from django.urls import path
from .views import RestaurantsListViews, RestaurantMenu, OrderCreateView, OrderListView, UpdateOrderView, \
    OrderDeleteView

app_name = 'food_delivery'

urlpatterns = [
    path('rests/',RestaurantsListViews.as_view(),name = 'rests'),
    path('rests/menu_<int:pk>',RestaurantMenu.as_view(), name = 'rest_menu'),
    path('rests/create_order_<int:pk>',OrderCreateView.as_view(),name = 'create_order'),
    path('orders/', OrderListView.as_view(), name='orders_list'),
    path('rests/update_order_<int:pk>', UpdateOrderView.as_view(), name='update_order'),
    path('rests/delete_order_<int:pk>', OrderDeleteView.as_view(), name='delete_order'),


]