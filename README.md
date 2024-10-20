6 урок ДЗ

Объединенный фильтр названия и адреса ресторанов. 
До фильтра:
![image](https://github.com/user-attachments/assets/950056ad-70f8-4db3-9df1-d6a3c161a8d1)
После фильтра:
![image](https://github.com/user-attachments/assets/bd5bd83f-4b8e-402d-b156-244434c65c46)
![image](https://github.com/user-attachments/assets/d7ea9042-df33-47a7-b13e-719d6cbaffad)

Фильтр диапазона цены и булевый фильтр вегетарианского блюда. До фильтра:
![image](https://github.com/user-attachments/assets/1cdd4823-fb9e-4ceb-a170-7dc15d55511d)

После фильтра:
![image](https://github.com/user-attachments/assets/548fc5b2-b5d7-436a-9c05-dcffebe87a67)

![image](https://github.com/user-attachments/assets/d622ed21-4fa6-45ef-b4fd-1495f6f13e8f)

Фильтр названия ресторана в заказе и булевый фильтр большой ли заказ (>=3 считается большим). До фильтра:
![image](https://github.com/user-attachments/assets/501d55e1-2e02-4b2a-903c-31466b3979d0)

После фильтра;
![image](https://github.com/user-attachments/assets/2540b6a3-3b64-4f71-8e37-916e1c041495)

![image](https://github.com/user-attachments/assets/2f9fbc1f-c1f0-455d-ae06-8b0dcf88255c)























from site_delivery.wsgi import *

from food_delivery import models

from django.db.models import Q

from django.db.models import Sum,Count, Avg, Min, Max


1 Задание (Добавление объектов и получение всех записей модели)


![image](https://github.com/user-attachments/assets/c6d68d50-4761-4410-bbe5-351c64b64481)
![image](https://github.com/user-attachments/assets/c8cb84be-930b-4570-bf10-f701db3b878e)
![image](https://github.com/user-attachments/assets/bed9c3c2-971b-4faf-8136-86562db6a045)
![image](https://github.com/user-attachments/assets/051f2492-bc73-4c0f-bb41-14711c72e388)


2 задание (Сложные запросы с filter(),exclude(),order_by())

Получение записей модели Курьеры, номера которых начинаются на +795, сортировка по фамилии

![image](https://github.com/user-attachments/assets/cb552b39-e812-4a11-b4ad-3ea2f69d404e)

Получение записей модели Меню, цена которых от 400 до 650 включительно, сортировка по названию

![image](https://github.com/user-attachments/assets/770358fc-988c-4b5a-9182-51ceda529c77)

Получение записей модели Меню, содержащих в составе "помидоры", кроме категории "Салат", сортировка по названию

![image](https://github.com/user-attachments/assets/eb3cf146-0629-4d19-a939-55900fc8d64f)

Получение записей модели Пользователи, кроме тех, у которых email = NULL, сортировка по имени

![image](https://github.com/user-attachments/assets/b43c22fe-6488-4af2-988c-2e79502eae73)

3 задание (Запросы через связь. values() и values_list())


Привязка другого склада(id_warehouse = 9) к ресторану (id_rest = 4)

![image](https://github.com/user-attachments/assets/8d10cfd6-23b7-4cc0-b6ba-38ccbed329f1)

Привязка другого ресторана(id_rest = 4) к блюду (id_dish = 9)

![image](https://github.com/user-attachments/assets/afeb01be-2f2c-4721-b696-cab7edc4a228)

Добавление нового блюда (id_dish = 7) в уже существующий заказ (id_order = 4)

![image](https://github.com/user-attachments/assets/a39a6dd6-a5a1-4367-a9f7-809e71ee44ab)

Получение всех записей модели Меню (Название, цена)

![image](https://github.com/user-attachments/assets/04efbc3d-70cf-4069-98a8-205f9bf20d46)

Получение всех записей модели Рестораны (Название, адрес)

![image](https://github.com/user-attachments/assets/ba8006f1-b27b-439f-a260-5560447ad441)

Получение всех записей модели Пользователи (Имя, Фамилия, адрес)

![image](https://github.com/user-attachments/assets/c910de81-3c2c-4176-9b52-e506aa14b15f)

Получение всех записей модели Склад в виде кортежа (Название, адрес)

![image](https://github.com/user-attachments/assets/fee6a549-979d-4a9f-b58a-bfe62fd93b67)

Получение всех записей модели Курьеры в виде кортежа (Имя, Фамилия, телефон)

![image](https://github.com/user-attachments/assets/5335aaef-e8fa-4147-b60b-a3eb6f2ad4c0)

Получение всех записей модели Меню в виде кортежа (Название, категория)

![image](https://github.com/user-attachments/assets/ac634678-76ab-4646-8f62-cd36da864ff0)


4 задание (Запросы с Q объектами для сложных условий)

Получение записей модели Курьеры, имя которых или "Роман", или номер содержит "+794"

![image](https://github.com/user-attachments/assets/26051f49-eb5b-4d90-9a14-f62ad3b46b0b)

Получение записей модели Меню, если в названии есть "роллы" или категория "Салат"

![image](https://github.com/user-attachments/assets/dc29cefd-6fa6-45e7-83eb-6846a668189c)

Получение записей модели Меню, если цена <= 500 или категория "Суп"

![image](https://github.com/user-attachments/assets/cc777258-5f0e-4945-b515-7bb0f5367554)

Получение записей модели Меню, если категория "Закуска" И цена >= 600

![image](https://github.com/user-attachments/assets/93ec67ef-007d-4533-b243-523aab5e0e77)

Получение записей модели Меню, если категория "Закуска" И в составе есть "сыр"

![image](https://github.com/user-attachments/assets/c425ee4d-46a5-4f33-a775-5d1d95c35f21)

Получение записей модели Пользователи, если в адресе есть "15" и email = NULL

![image](https://github.com/user-attachments/assets/17409e1e-754f-4386-936f-bb8da51f4a5a)

Получение записей модели Меню, если категория "Закуска" ИЛИ "Выпечка", кроме тех, чья цена >=600

![image](https://github.com/user-attachments/assets/77b075c0-ccfa-469b-9fa9-f4658dae1d32)

Получение записей модели Пользователи, если адрес содержит "10" ИЛИ "15", кроме тех, у кого email = NULL ИЛИ содержит "yandex"

![image](https://github.com/user-attachments/assets/31daec22-4cc4-4820-bd81-fd6f2b217be1)

Получение записей модели Меню, если в составе есть "помидоры", кроме категории "Салат" ИЛИ цена >= 600

![image](https://github.com/user-attachments/assets/9ab1d62c-4c70-4f8c-8d22-e12ee472e14b)


5 задание (работа с агрегированными данными с помощью методов annotate() и aggregate())

5.1 annotate()

Средняя цена блюд в каждом ресторане

![image](https://github.com/user-attachments/assets/079d55be-3906-44d3-b5b2-fc5a1a64b50d)

Максимальная и минимальная цена в каждой категории модели Меню

![image](https://github.com/user-attachments/assets/bbc43db7-9e44-4606-96f9-87c4d38ce209)

Количество блюд в каждом ресторане

![image](https://github.com/user-attachments/assets/b954b404-d916-4865-b01c-e51f0a4b8c4a)

5.2 aggregate()

Общее количество заказов модели Заказы

![image](https://github.com/user-attachments/assets/8a671624-27a2-415d-be8c-85a91c64231c)

Общее количество пользователей модели Пользователи

![image](https://github.com/user-attachments/assets/9ded5bc7-2d76-4e03-8443-30de05da1803)

Цена самого дорого блюда модели Меню

![image](https://github.com/user-attachments/assets/10659602-f63a-45af-a3ea-3e9bee4cb1e9)














































