import django_filters
import food_delivery.models
from django.db.models import Q, Count
from django import forms

class RestsFilter(django_filters.FilterSet):
    term = django_filters.CharFilter(method = 'filter_term', label = 'Поиск')

    def filter_term(self,queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(name__icontains = term) | Q(address__icontains = term)
        return queryset.filter(criteria).distinct()

    class Meta:
        model = food_delivery.models.Restaurant
        fields = ['term']

class MenuFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter(field_name='price', label = 'Цена от и до',
                                       widget=django_filters.widgets.RangeWidget(attrs={'class': 'form-control'}))
    vegetarian = django_filters.BooleanFilter(method='filter_vegetarian', label='Вегетарианское')

    class Meta:
        model = food_delivery.models.Menu
        fields = ['price']

    def filter_vegetarian(self, queryset, name, value):
        ban_list = ['мясо', 'говядина', 'свинина', 'рыба', 'тунец', 'лосось',
                    'икра', 'котлета', 'котлета', 'бекон','фарш','курица','куриные','крылышки','говяжий','стейк','Тунец']

        if value:
            for item in ban_list:
                queryset = queryset.exclude(composition__icontains=item)
            return queryset
        return queryset

class OrderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='Название',field_name='id_rest__name',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    big_order = django_filters.BooleanFilter(method='filter_is_big_order',label = 'Большой заказ')

    class Meta:
        model = food_delivery.models.Order
        fields = ['name','big_order']

    def filter_is_big_order(self, queryset, name, value):
        if value:
            return queryset.annotate(dish_count=Count('dishes')).filter(dish_count__gte=3)
        return queryset
