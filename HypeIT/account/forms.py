from django import forms
from .models import City, Department, Staff, Profile 

class SearchForm(forms.Form):
    searchText = forms.CharField(max_length=60, required=False)

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department']

'''class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['fName', 'lName', 'email', 'city', 'department', 'comment']
        
        labels = {
            'fName' : '', 
            'lName' : '', 
            'email' : '', 
            'city' : '', 
            'department' : '', 
            'comment' : ''
        }'''