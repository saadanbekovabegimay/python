import django_filters
from .models import Vacancy

class VacancyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr ='lt')
    experience__gt = django_filters.NumberFilter(field_name='experience', lookup_expr='gt')
    experience__lt = django_filters.NumberFilter(field_name='experience', lookup_expr='lt')

    skills = django_filters.CharFilter(field_name='skills', lookup_expr='icontains')

    class Meta:
        model = Vacancy
        fields = ['title']
