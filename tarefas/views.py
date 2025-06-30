from django.shortcuts import render

from .models import Tarefa


def tarefas_lista(request):
    tarefas = Tarefa.objects.all()
    return render(request, "tarefas/tarefas_lista.html", {"tarefas": tarefas})
