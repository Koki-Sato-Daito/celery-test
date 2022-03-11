from django import forms
from demoapp.models import Widget



class WidgetForm(forms.ModelForm):
    class Meta:
        model = Widget
        fields = ['name']
