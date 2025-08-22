from django.urls import path
from .views import *

app_name = "persona"


urlpatterns = [
    path(
        "lista/",
        PersonaListView.as_view(),
        name="lista_personas"
    ),
    path(
        "detalle/<int:pk>/",
        PersonaDetailView.as_view(),
        name="detalle_persona"
    )
]
