from django.contrib import admin
from django.urls import path

from tarefas.views import TarefaCreateView, TarefaListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TarefaListView.as_view(), name="tarefa_list"),
    path("create", TarefaCreateView.as_view(), name="tarefa_create"),
]
