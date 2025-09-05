from django import forms
from .models import UtilitarioCarga

class UtilitarioCargaForm(forms.ModelForm):
    class Meta:
        model = UtilitarioCarga
        fields = "__all__"
