
from django.db import models

#функция создания пути для файла превью
def menu_preview_directory_path(instance:"Menu",filename:str) -> str:
    return f'menu/previews/dish_{filename}'

def rest_photo_directory_path(instance:"Restaurant",filename:str) -> str:
    return f'restaurants/photo/{filename}'

category_dishes = [
    ("Закуска", "Закуска"),
    ("Суп", "Суп"),
    ("Напиток", "Напиток"),
    ("Десерт", "Десерт"),
    ("Гарнир", "Гарнир"),
    ("Салат", "Салат"),
    ("Выпечка", "Выпечка"),
]


class User(models.Model):
    id_user = models.AutoField(auto_created = True, primary_key = True,verbose_name = 'id пользователя')
    first_name = models.CharField(max_length=50,verbose_name='имя пользователя')
    surname = models.CharField(max_length=60,verbose_name='фамилия пользователя', blank = True)
    address = models.CharField(max_length=100,verbose_name='адрес пользователя')
    email = models.EmailField(max_length=254,unique=True,verbose_name='email пользователя', blank=True, null = True)
    phone_number = models.CharField(max_length=20,unique=True,verbose_name='номер телефона')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['first_name']

    def __str__(self):
        return f'{self.first_name} {self.surname}'

class Warehouse(models.Model):
    id_warehouse = models.AutoField(auto_created = True, primary_key = True,verbose_name = 'id склада')
    name = models.CharField(max_length=80,verbose_name='наименование склада')
    address = models.CharField(max_length=100,verbose_name='адрес склада')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ['id_warehouse']

    def __str__(self):
        return f'{self.name} {self.address}'

class Restaurant(models.Model):
    id_rest = models.AutoField(auto_created=True, primary_key=True, verbose_name='id ресторана')
    name = models.CharField(max_length=80,verbose_name='название ресторана')
    address = models.CharField(max_length=100,verbose_name='адрес ресторана')
    photo_rest = models.ImageField(null = True, blank = True, upload_to=rest_photo_directory_path, verbose_name='фото ресторана')

    id_warehouse = models.OneToOneField(
        Warehouse,
        verbose_name='склад',
        related_name='restaurant',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.address}'

class Courier(models.Model):
    id_cour = models.AutoField(auto_created=True, primary_key=True, verbose_name='id курьера')
    first_name = models.CharField(max_length=50,verbose_name='имя курьера')
    surname = models.CharField(max_length=60,verbose_name='фамилия курьера', blank = True)
    phone_number = models.CharField(max_length=20, unique=True,verbose_name='телефон курьера')

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'
        ordering = ['first_name']

    def __str__(self):
        return f'{self.first_name} {self.surname}'

class Menu(models.Model):
    id_dish = models.AutoField(auto_created = True, primary_key = True,verbose_name = 'id блюда')
    name = models.CharField(max_length=90,verbose_name='название блюда')
    category = models.CharField(max_length=40,verbose_name='категория', choices=category_dishes)
    composition  = models.TextField(verbose_name='состав блюда')
    price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='цена блюда',null=True)
    preview = models.ImageField(null = True, blank = True,upload_to=menu_preview_directory_path,verbose_name='фото блюда')
    id_rest = models.ForeignKey(
        Restaurant,
        verbose_name='ресторан',
        related_name='menu',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    # метод проверки является ли блюдо вегетерианским
    def is_vegetarian(self):
        forbidden_ingredients = ["мясо", "курица", "рыба", "говядина", "свинина"]
        for ingredient in forbidden_ingredients:
            if ingredient in self.composition.lower():
                return False
        return True

class Order(models.Model):
    id_order = models.AutoField(auto_created=True, primary_key=True, verbose_name='id заказа')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='дата создания заказа')
    promocode = models.CharField(max_length=10,verbose_name='промокод', blank = True)
    comment = models.TextField(verbose_name='комментарий к заказу',blank=True)
    dishes = models.ManyToManyField(
        Menu,
        verbose_name='заказанные блюда',
        related_name='orders',
    )
    id_user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        related_name='orders',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    id_cour = models.ForeignKey(
        Courier,
        verbose_name='курьер',
        related_name='orders',
        null = True,
        blank= True,
        on_delete=models.SET_NULL
    )
    id_rest = models.ForeignKey(
        Restaurant,
        verbose_name='ресторан',
        related_name= 'orders',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.created_at} {self.dishes} {self.comment}'

    # метод подсчета общей суммы заказа
    def calculation_order_amount(self):
        amount = 0
        for dish in self.dishes.all():
            if dish.price:
                amount += dish.price
        if self.promocode:
            amount = amount*0.9
        return amount


