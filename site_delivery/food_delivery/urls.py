from django.urls import path
from food_delivery.views import (RestaurantsListViews,
                                 RestaurantMenu,
                                 OrderCreateView,
                                 OrderListView,
                                 UpdateOrderView,
                                 OrderDeleteView,
                                 RestaurantAPI,
                                 MenuAPI,
                                 OrderAPI,)

from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name = 'food_delivery'

router = DefaultRouter()
router.register('rests_api',RestaurantAPI, basename = 'rests_api')
router.register('menu_api',MenuAPI,basename='menu_api')
router.register('order_api',OrderAPI,basename='order_api')

urlpatterns = [
    path('rests/',RestaurantsListViews.as_view(),name = 'rests'),
    path('rests/menu_<int:pk>',RestaurantMenu.as_view(), name = 'rest_menu'),
    path('rests/create_order_<int:pk>',OrderCreateView.as_view(),name = 'create_order'),
    path('orders/', OrderListView.as_view(), name='orders_list'),
    path('rests/update_<int:pk>', UpdateOrderView.as_view(), name='update_order'),
    path('rests/delete_order_<int:pk>', OrderDeleteView.as_view(), name='delete_order'),
    path('schema/', SpectacularAPIView.as_view(), name = 'schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name = 'food_delivery:schema')),

] + router.urls