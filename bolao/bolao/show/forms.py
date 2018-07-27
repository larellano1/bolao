from django import forms
from .models import Bolao

class ConvidarAmigo(forms.Form):
    nome_amigo = forms.CharField(label="Nome do amigo:", max_length = 200)
    email_amigo = forms.EmailField(label="E-mail do Amigo:")
    mensagem = forms.CharField(label="Escreva uma mensagem:", widget=forms.Textarea)

class BolaoForm(forms.ModelForm):
    class Meta:
        model = Bolao
        fields = ["nome", "campeonato", "participantes", "regulamento", "premiacao", "imagem", "valor_entrada"]