from django.shortcuts import render


def tarefas_lista(request):
    return render(request, "tarefas/tarefas_lista.html")
