import csv
import sys
from django.db import transaction
from django.core.exceptions import ValidationError
from oficina.models import Oficina 
from persona.models import Persona

def run(*args):
    if not args:
        print("Error: Por favor, proporciona la ruta al archivo CSV.")
        print("Uso: python manage.py runscript import_personas --script-args <ruta_al_archivo_csv>")
        sys.exit(1)

    csv_file = args[0]

    oficinas_map = {oficina.nombre_corto: oficina for oficina in Oficina.objects.all()}

    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            personas_a_crear = []

            for row in reader:
                nombre = row.get('nombre')
                apellido = row.get('apellido')
                edad = row.get('edad')
                oficina_nombre_corto = row.get('oficina_nombre_corto')

                if not nombre or not apellido or not edad:
                    print(f"Error en la fila {row}. Falta el nombre, apellido o edad.")
                    continue

                try:
                    edad_int = int(edad)
                except (ValueError, TypeError):
                    print(f"Error en la fila {row}. Edad no es un número válido.")
                    continue

                oficina_obj = None
                if oficina_nombre_corto:
                    oficina_obj = oficinas_map.get(oficina_nombre_corto)
                    if not oficina_obj:
                        print(f"Error en la fila {row}. Oficina con nombre corto '{oficina_nombre_corto}' no encontrada.")
                        print(f"Se creara el registro sin oficina.")

                else:
                    print(f"Advertencia: La persona '{nombre} {apellido}' no tiene una oficina asignada. Se creara sin oficina.")

                try:
                    persona = Persona(nombre=nombre, apellido=apellido, edad=edad_int, oficina=oficina_obj)
                    persona.full_clean()  # Validar el modelo
                    personas_a_crear.append(persona)
                except ValidationError as e:
                    print(f"Error de validación en la fila {row}: Detalle: {e}")
                except Exception as e:
                    print(f"Error inesperado en la fila {row}: Detalle: {e}")

            with transaction.atomic():
                Persona.objects.bulk_create(personas_a_crear)
                print(f"Se importaron {len(personas_a_crear)} registros.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {csv_file}.")
    except Exception as e:
        print(f"Error inesperado en la importacion: {e}")
        
