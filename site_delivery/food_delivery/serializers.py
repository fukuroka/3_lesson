from rest_framework import serializers
from food_delivery import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = '__all__'


class CourierSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Courier
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    #id_rest = RestaurantSerializer(read_only=True)
    class Meta:
        model = models.Menu
        fields = ('name','composition','price','preview','id_rest')

# простой сериализатор Ресторана для отображения в api заказов, чтобы не было лишней информации
class SimpleRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ('id_rest', 'name', 'address', 'photo_rest')

class RestaurantSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True, many=True)
    class Meta:
        model = models.Restaurant
        fields = ('id_rest','name','address','photo_rest','menu')


class OrderSerializers(serializers.ModelSerializer):
    id_user = UserSerializer(read_only=True)
    id_cour = CourierSerializer(read_only=True)
    id_rest = SimpleRestaurantSerializer(read_only=True)
    dishes = MenuSerializer(many=True,read_only=True)
    is_large = serializers.SerializerMethodField()
    class Meta:
        model = models.Order
        fields = ('id_order','created_at','promocode','comment','id_user','id_cour','id_rest','dishes','is_large')

    # метод для определения больших заказов
    def get_is_large(self,obj):
        if obj.dishes.count() >=3:
            return True
        return False
