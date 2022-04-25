from django import forms
from .models import Warehouse, Preparing, InUse, Retired


class DateInput(forms.DateInput):
    input_type = 'date'

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"
        widgets = {
            'orderDate': DateInput(),
        }


class PrepareForm(forms.ModelForm):
    class Meta:
        model = Preparing
        fields = "__all__"


class InUseForm(forms.ModelForm):
    class Meta:
        model = InUse
        fields = "__all__"
        widgets = {
            'date': DateInput(),
        }


class RetiredForm(forms.ModelForm):
    class Meta:
        model = Retired
        fields = "__all__"
        widgets = {
            'date': DateInput(),
        }