from django import forms
from django.forms import ModelForm
from accounts.models import EmployeeModel


class EmployeeForm(ModelForm):

    class Meta:
        model = EmployeeModel
        widgets = {
            'person': forms.Select(attrs={'class': 'form-select'}),
            'status_employee': forms.Select(attrs={'class': 'form-select'}),
            'function': forms.Select(attrs={'class': 'form-select'}),
        }

        fields = [
            'person',
            'status_employee',
            'function'
        ]
