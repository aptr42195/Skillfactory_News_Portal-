<<<<<<< HEAD
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

=======
from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
>>>>>>> 8dc332dc15bc6b6b2a0e0bca3cad4c6cd45214fd
    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
<<<<<<< HEAD
=======
           'author': ['in'],
           # 'data_creations': ['gt']
>>>>>>> 8dc332dc15bc6b6b2a0e0bca3cad4c6cd45214fd
       }