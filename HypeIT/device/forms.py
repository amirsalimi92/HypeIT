from django import forms
from .models import Pc

class PcForm(forms.ModelForm):
    class Meta:
        model = Pc
        fields = "__all__"