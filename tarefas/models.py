from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    criada_em = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    prazo = models.DateTimeField(null=False, blank=False)
    concluida_em = models.DateTimeField(null=True)
