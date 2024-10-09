from django.contrib import admin
from food_delivery import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','surname','address','phone_number')

@admin.register(models.Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name','address')

@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','address')

@admin.register(models.Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('first_name','surname','phone_number')

@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','category','price')

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id_order','created_at','comment')
