from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Time(models.Model):
    nome = models.CharField(max_length = 200)
    imagem = models.CharField(max_length = 100, default = 'time_padrao.jpg')
    

    def __str__(self):
        return("{0}".format(self.nome))


class Modalidade(models.Model):
    nome = models.CharField(max_length = 100)


    def __str__(self):
        return("{0}".format(self.nome))


class Campeonato(models.Model):
    modalidade = models.ForeignKey(Modalidade, on_delete = models.CASCADE)
    data_inicio = models.DateField('data campeonato')
    nome = models.CharField(max_length = 200)
    times = models.ManyToManyField(Time)

    def __str__(self):
        return("{0} - Data: {1}".format(self.nome, self.data_inicio))

class Jogo(models.Model):
    times = models.ManyToManyField(Time)
    data = models.DateTimeField('data jogo')
    campeonato = models.ForeignKey(Campeonato, on_delete = models.CASCADE)

class Gol(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete = models.CASCADE)
    time = models.ForeignKey(Time, on_delete = models.CASCADE)

class Criterio(models.Model):
    criterio = models.CharField(max_length = 200)
    clausula = models.CharField(max_length = 1000)

    def __str__(self):
        return("{0}".format(self.criterio))


class Regra(models.Model):
    criterios = models.ForeignKey(Criterio,on_delete = models.CASCADE)
    pontuacao = models.IntegerField(default=5)


    def __str__(self):
        return("Critério: {0} - Pontuação: {1}".format(self.criterios, self.pontuacao))


class Regulamento(models.Model):
    regras = models.ManyToManyField(Regra)
    nome = models.CharField(default = "Padrão", max_length = 200)
 
    def __str__(self):
        return("Nome: {0}".format(self.nome))

class TiposPremiacao(models.Model):
    nome = models.CharField(max_length = 100)
    
    def __str__(self):
        return("Nome: {0}".format(self.nome))


class Premiacao(models.Model):
    tipo = models.ForeignKey(TiposPremiacao, on_delete = models.CASCADE)
    detalhes = models.CharField(default = '', max_length = 300)
    valor_total = models.DecimalField(decimal_places=2, max_digits=9, blank = True, null = True)

    def __str__(self):
        return("Tipo: {0} - Valor {1}".format(self.tipo, self.valor_total))

class Bolao(models.Model):
    nome = models.CharField(max_length = 200, default = "Bolão dos Amigos")
    campeonato = models.ForeignKey(Campeonato, on_delete = models.CASCADE)
    regulamento = models.ForeignKey(Regulamento, on_delete = models.CASCADE)
    participantes = models.ManyToManyField(User)
    premicacao = models.ManyToManyField(Premiacao)
    valor_entrada = models.DecimalField(decimal_places=2,max_digits=9, blank = True, null = True)
    aberto = models.BooleanField(default = False)
    imagem = models.CharField(max_length = 100, default = 'bolao_padrao.jpg')

    def __str__(self):
        return("Nome: {0}".format(self.nome))

class Palpites(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    gols = models.ForeignKey(Gol, on_delete = models.CASCADE)
    bolao = models.ForeignKey(Bolao, on_delete = models.CASCADE)

class Cartao(models.Model):
    nome_bandeira = models.CharField(max_length = 100)
    numero_internacional = models.IntegerField()

    def __str__(self):
        return("Nome: {0} - NI: {1}".format(self.nome_bandeira, self.numero_internacional))


class UsuarioDetalhes(models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 300)
    numero_cartao = models.BigIntegerField()
    bandeira_cartao = models.ForeignKey(Cartao, on_delete = models.CASCADE)
    imagem = models.CharField(max_length = 100, default = 'avatar.jpg')

    def __str__(self):
        return("Nome: {0}".format(self.nome))
