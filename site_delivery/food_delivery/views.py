from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

import food_delivery.models
from food_delivery.forms import OrderForm
from food_delivery.models import Restaurant, Order, User
from django_filters.views import FilterView
from food_delivery.filters import RestsFilter,MenuFilter, OrderFilter

class RestaurantsListViews(FilterView):
    template_name = 'food_delivery/restaurants_list.html'
    model = Restaurant
    context_object_name = 'rests'
    filterset_class = RestsFilter

class RestaurantMenu(DetailView):
    template_name = 'food_delivery/menu_list.html'
    model = Restaurant
    context_object_name = 'rest'

    def get_context_data(self, **kwargs):
        context_data = super(RestaurantMenu, self).get_context_data()
        rest_pk = self.kwargs.get('pk', None)
        f = MenuFilter(self.request.GET, queryset=food_delivery.models.Menu.objects.filter(id_rest=rest_pk))
        context_data['filter'] = f
        return context_data


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'food_delivery/order_form.html'

    success_url = reverse_lazy('food_delivery:rests')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['restaurant'] = Restaurant.objects.get(pk=self.kwargs['pk'])
        return kwargs

class UpdateOrderView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'food_delivery/order_form.html'
    success_url = reverse_lazy('food_delivery:orders_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['restaurant'] = self.object.id_rest
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'food_delivery/order_confirm_delete.html'
    success_url = reverse_lazy('food_delivery:orders_list')

    def get(self, request, *args, **kwargs):
        # Получите объект заказа для отображения в шаблоне
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, self.template_name, context)


class OrderListView(FilterView):
    model = Order
    template_name = 'food_delivery/orders_list.html'
    context_object_name = 'orders'
    filterset_class = OrderFilter