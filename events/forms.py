from django import forms
from .models import Projects


class NewProjForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
