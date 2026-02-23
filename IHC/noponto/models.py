from django.db import models

class Onibus(models.Model):
    modelo = models.CharField(max_length=150)
    placa = models.CharField(max_length=50)
    numero_veiculo = models.IntegerField()
    capacidade_total = models.IntegerField()
    ano = models.PositiveSmallIntegerField()
    acessibilidade = models.BooleanField()

class Linha(models.Model):
    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    tarifa = models.DecimalField(max_digits=6, decimal_places= 2
    ,verbose_name="Tarifa (R$)")

class Rota(models.Model):
    sentido = models.CharField(max_length=30)
    distancia = models.DecimalField(max_digits=6, decimal_places= 2)
    tempo = models.DurationField()
    linha = models.ForeignKey(Linha, on_delete= models.CASCADE)

class Horario(models.Model):
     horario_saida = models.TimeField()
     horario_chegada = models.TimeField()
     dia_semana = models.CharField(max_length=15)
     linha = models.ForeignKey('Linha', on_delete=models.CASCADE)
     rota = models.ForeignKey('Rota', on_delete=models.CASCADE)
     onibus = models.ForeignKey('Onibus', on_delete=models.CASCADE)
        