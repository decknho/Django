from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Tarefa

class TarefaListView(ListView):
    model = Tarefa


class TarefaCreateView(CreateView):
    model = Tarefa
    fields = ["titulo", "prazo"]
    success_url = reverse_lazy("tarefa_list")

