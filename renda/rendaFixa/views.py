from django.shortcuts import render
from django.views import View
from .forms import InvestimentoForm
import json

# Create your views here.
class CalculadoraView(View):
    def get(self, request):
        form = InvestimentoForm()
        return render(request, 'renda.html', {'form': form})

    def post(self, request):
        form = InvestimentoForm(request.POST)
        resultado = None

        if form.is_valid():
            investimento_inicial = form.cleaned_data['investimento_inicial']
            taxa_juros = form.cleaned_data['taxa_juros'] / 100  
            anos = form.cleaned_data['anos']
            meta = form.cleaned_data['meta']

            montante = investimento_inicial * ((1 + taxa_juros) ** anos)
            
            labels_ano = list(range(1, anos + 1))
            valores_anuais = [str(investimento_inicial * (1 + taxa_juros) ** ano) for ano in labels_ano]
            
            resultado = {
                'montante': montante,
                'meta_alcancada': montante >= meta,
                'meta': meta,
                'valores_anuais': json.dumps(valores_anuais),
                'labels_ano': json.dumps(labels_ano)
            }

        return render(request, 'renda.html', {'form': form, 'resultado': resultado})