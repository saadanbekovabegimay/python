from django import forms
from .models import Vacancy


class VacancyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-input"}))

    class Meta:
        model = Vacancy
        fields = [
            'title',
            'salary',
            'description',
            'email',
            'contacts'
        ]
