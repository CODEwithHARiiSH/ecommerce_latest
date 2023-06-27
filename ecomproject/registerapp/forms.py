from .models import Payment

from django import forms


class dataForm(forms.ModelForm):
    class Meta:
        model = datas
        fields = ['cod', 'debit', 'credit', 'emi']
