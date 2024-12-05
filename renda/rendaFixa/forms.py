from django import forms

class InvestimentoForm(forms.Form):
    investimento_inicial = forms.DecimalField(
        label='Investimento Inicial',
        max_digits=12,
        decimal_places=2,
        widget=forms.TextInput(attrs={'placeholder': 'R$ 0,00', 'class': 'form-control'}),
    )
    taxa_juros = forms.DecimalField(
        label='Taxa de Juros',
        max_digits=5,
        decimal_places=2,
        widget=forms.TextInput(attrs={'placeholder': '0%', 'class': 'form-control'}),
    )
    anos = forms.IntegerField(
        label='Anos',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
    meta = forms.DecimalField(
        label='Meta',
        max_digits=12,
        decimal_places=2,
        widget=forms.TextInput(attrs={'placeholder': 'R$ 0,00', 'class': 'form-control'}),
    )
