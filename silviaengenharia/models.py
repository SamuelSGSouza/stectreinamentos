from django.db import models
from django import forms

class PaginaCliente(models.Model):
    preco_antigo = models.CharField(max_length=12)
    preco_novo = models.CharField(max_length=12)
    video_apresentacao = models.FileField(blank=True, upload_to="static/videos/videos_depoimentos")
    titulo_video_1 = models.CharField(max_length=255, blank=True)
    video_depoimento_1 = models.FileField(blank=True, upload_to="static/videos/videos_depoimentos")
    titulo_video_2 = models.CharField(max_length=255, blank=True)
    video_depoimento_2 = models.FileField(blank=True, upload_to="static/videos/videos_depoimentos")
    titulo_video_3 = models.CharField(max_length=255, blank=True)
    video_depoimento_3 = models.FileField(blank=True, upload_to="static/videos/videos_depoimentos")
    titulo_video_4 = models.CharField(max_length=255, blank=True)
    video_depoimento_4 = models.FileField(blank=True, upload_to="static/videos/videos_depoimentos")

    def __str__(self):
        return "Pagina Inicial"

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ()

class Email(models.Model):
    login = models.CharField(max_length=255, verbose_name='Login')
    senha = models.CharField(max_length=255, verbose_name='Senha')
    assunto = models.CharField(max_length=255, verbose_name='Assunto')
    mensagem = models.TextField(blank=True, verbose_name='Mensagem')

    def __str__(self):
        return "Email de Cadastro"

class MensagemParaTodos(models.Model):
    mensagem = models.TextField(blank=True, verbose_name='Mensagem')

    def __str__(self):
        return 'Mensagem para todos'
