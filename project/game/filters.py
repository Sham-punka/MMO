from django_filters import FilterSet, DateTimeFilter, CharFilter, ChoiceFilter, ModelChoiceFilter, AllValuesFilter
from django.forms import DateTimeInput, CharField
from django.contrib.auth.models import User
import django_filters
from .models import *


class PostFilter(FilterSet):

    category = ChoiceFilter(
        choices=Post.CATEGORY_CHOICES,
        label='Категории')

    added_after = DateTimeFilter(
        label='Дата публикации после',
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%d-%m-%Y',
            attrs={'type': 'datetime-local'},
        ),
    )


class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = [
            'post'
        ]

        label = {
            'author': 'A',
        }

    post = AllValuesFilter(
        field_name='post__title',
        label= 'Объявлениея',

    )

    author = AllValuesFilter(
        field_name='author__username',
        label='Автор',
    )

    # category = django_filters.ChoiceFilter(
    #     choices=Response.,
    #     label='Категории')

    added_after = DateTimeFilter(
        label='Дата публикации после',
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%d-%m-%Y',
            attrs={'type': 'datetime-local'},
        ),
    )