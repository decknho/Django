from django.db import models

class Cliente(models.Model):
    CPF = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class Pagamento(models.Model):
    FORMA_CHOICES = [
        ('Cartão', 'Cartão'),
        ('Pix', 'Pix'),
        ('Dinheiro', 'Dinheiro'),
    ]
    ESTADO_CHOICES = [
        ('Pago', 'Pago'),
        ('Pendente', 'Pendente'),
    ]

    forma = models.CharField(max_length=10, choices=FORMA_CHOICES)
    dataPagamento = models.DateField(blank=True, null=True)
    valorTotal = models.DecimalField(max_digits=7, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def __str__(self):
        return f'{self.forma} - {self.estado}'


class Veiculo(models.Model):
    ESTADO_CHOICES = [
        ('Disponível', 'Disponível'),
        ('Alugado', 'Alugado'),
        ('Manutenção', 'Manutenção'),
    ]

    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10, unique=True)
    valorDiaria = models.DecimalField(max_digits=7, decimal_places=2)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES)

    def __str__(self):
        return f'{self.modelo} - {self.placa}'


class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.SET_NULL, null=True, blank=True)
    dataInicio = models.DateField()
    dataFim = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Locação #{self.id} - {self.cliente.nome}'


class LocacaoVeiculo(models.Model):
    locacao = models.ForeignKey(Locacao, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('locacao', 'veiculo')

    def __str__(self):
        return f'{self.locacao} -> {self.veiculo}'


class Manutencao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    dataManutencao = models.DateField()
    custo = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.veiculo} - {self.dataManutencao}'
