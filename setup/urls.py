from django.contrib import admin
from django.urls import path

from tarefas.views import tarefas_lista

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", tarefas_lista, name="tarefas_lista")
]
