from django.forms import ModelForm
from dashboard.models import Barang,Jenis
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.NumberInput({'class':'form-control'}),
            'harga': forms.NumberInput({'class':'form-control'}),
            'link_gbr': forms.FileInput({'class':'form-control'}),
            'jenis_id': forms.Select({'class':'form-control'}),
        }

class FormJenis(forms.ModelForm):
    class Meta:
        model = Jenis
        fields = ['nama', 'ket']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'ket': forms.Textarea(attrs={'class': 'form-control'}),
        }