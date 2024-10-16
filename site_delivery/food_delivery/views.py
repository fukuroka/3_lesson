from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from food_delivery.forms import OrderForm
from food_delivery.models import Restaurant, Order, User


class RestaurantsListViews(ListView):
    template_name = 'food_delivery/restaurants_list.html'
    model = Restaurant
    context_object_name = 'rests'

class RestaurantMenu(DetailView):
    template_name = 'food_delivery/menu_list.html'
    model = Restaurant
    context_object_name = 'rest'


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
        kwargs['restaurant'] = self.object.id_rest  # Передаем ресторан из объекта Order
        return kwargs

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'food_delivery/order_confirm_delete.html'  # Добавьте шаблон для подтверждения удаления
    success_url = reverse_lazy('food_delivery:orders_list')

class OrderListView(ListView):
    model = Order
    template_name = 'food_delivery/orders_list.html'
    context_object_name = 'orders'