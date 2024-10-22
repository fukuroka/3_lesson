import factory
from factory.django import ImageField
from factory.fuzzy import FuzzyDecimal
from food_delivery import models



class RestaurantFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('company')
    address = factory.Faker('address')
    photo_rest = ImageField()
    class Meta:
        model = models.Restaurant


class MenuFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    category = factory.Faker('word')
    composition = factory.Faker('sentences')
    price = FuzzyDecimal(low=200, high=700, precision=2)
    preview = ImageField()
    id_rest = factory.SubFactory(RestaurantFactory)

    class Meta:
        model = models.Menu

class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    address = factory.Faker('address')
    email = factory.Faker('email')
    phone_number = factory.Faker('phone_number')

    class Meta:
        model = models.User

class CourierFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    surname = factory.Faker('last_name')

    class Meta:
        model = models.Courier

class OrderFactory(factory.django.DjangoModelFactory):
    created_at = factory.Faker('date')
    promocode = factory.Faker('word')
    comment = factory.Faker('sentences')
    dishes = factory.RelatedFactory(MenuFactory, 'orders', size=3)
    id_user = factory.SubFactory(UserFactory)
    id_cour = factory.SubFactory(CourierFactory)
    id_rest = factory.SubFactory(RestaurantFactory)

    # для корректного добавления блюд используем @factory.post_generation, т.к. связь модели Order с моделью Menu - многие-ко-многим
    @factory.post_generation
    def dishes(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.dishes.set(extracted)

        else:
            for i in range(3):
                self.dishes.add(MenuFactory())

    class Meta:
        model = models.Order
