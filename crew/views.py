from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from crew.crew import SearchCrew
from crew.forms import PerguntaForm
from crew.models import Vendas

# Create your views here.
class IndexView(FormView):
    template_name = 'index.html'
    form_class = PerguntaForm
    
    def form_valid(self, form):
        pergunta = form.cleaned_data['pergunta']

        vendas = Vendas.objects.all()
        dados_formatados = vendas.values_list('nome', 'quantidade', 'preco', 'total')

        crew = SearchCrew(pergunta, dados_formatados)
        result = crew.run()

        return self.render_to_response(self.get_context_data(result=result))
        
    
