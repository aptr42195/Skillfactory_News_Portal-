from django.contrib.auth.models import User
from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from .models import Post
from django.forms import DateInput

class PostFilter(FilterSet):
    author__user = ModelChoiceFilter(
        field_name = 'author__author',
        queryset=User.objects.all(),
        label='Автор',
    )
    time_in = DateFilter(
        lookup_expr='gt',
        widget=DateInput(),
        label='Дата',
    )

    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
       }