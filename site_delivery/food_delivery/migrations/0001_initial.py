# Generated by Django 5.1.2 on 2024-10-08 18:29

import django.db.models.deletion
import food_delivery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id_cour', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id курьера')),
                ('first_name', models.CharField(max_length=50, verbose_name='имя курьера')),
                ('surname', models.CharField(blank=True, max_length=60, verbose_name='фамилия курьера')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='телефон курьера')),
            ],
            options={
                'verbose_name': 'Курьер',
                'verbose_name_plural': 'Курьеры',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id_rest', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id ресторана')),
                ('name', models.CharField(max_length=80, verbose_name='название ресторана')),
                ('address', models.CharField(max_length=100, verbose_name='адрес ресторана')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Рестораны',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id пользователя')),
                ('first_name', models.CharField(max_length=50, verbose_name='имя пользователя')),
                ('surname', models.CharField(blank=True, max_length=60, verbose_name='фамилия пользователя')),
                ('address', models.CharField(max_length=100, verbose_name='адрес пользователя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email пользователя')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='номер телефона')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id_warehouse', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id склада')),
                ('name', models.CharField(max_length=80, verbose_name='наименование склада')),
                ('address', models.CharField(max_length=100, verbose_name='адрес склада')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
                'ordering': ['id_warehouse'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_dish', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id блюда')),
                ('name', models.CharField(max_length=90, verbose_name='название блюда')),
                ('category', models.CharField(choices=[('Закуска', 'Закуска'), ('Суп', 'Суп'), ('Напиток', 'Напиток'), ('Десерт', 'Десерт'), ('Гарнир', 'Гарнир'), ('Салат', 'Салат'), ('Выпечка', 'Выпечка')], max_length=40, verbose_name='категория')),
                ('composition', models.TextField(verbose_name='состав блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='цена блюда')),
                ('preview', models.ImageField(blank=True, null=True, upload_to=food_delivery.models.menu_preview_directory_path, verbose_name='фото блюда')),
                ('id_rest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menu', to='food_delivery.restaurant', verbose_name='ресторан')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id заказа')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания заказа')),
                ('promocode', models.CharField(blank=True, max_length=10, verbose_name='промокод')),
                ('comment', models.TextField(blank=True, verbose_name='комментарий к заказу')),
                ('dishes', models.ManyToManyField(related_name='orders', to='food_delivery.menu', verbose_name='заказанные блюда')),
                ('id_cour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='food_delivery.courier', verbose_name='курьер')),
                ('id_rest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='food_delivery.restaurant', verbose_name='ресторан')),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='food_delivery.user', verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='id_warehouse',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant', to='food_delivery.warehouse', verbose_name='склад'),
        ),
    ]
