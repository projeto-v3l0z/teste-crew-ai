from django import forms
from crew.models import Pergunta


class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta 
        fields = ['pergunta']

        widgets = {
            'pergunta': forms.Textarea(attrs={'class': 'form-control'})
        }