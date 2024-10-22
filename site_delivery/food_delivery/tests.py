
from django.urls import reverse
from django.test import TestCase
from food_delivery import factories, models


class FoodDeliveryTestCase(TestCase):
    def setUp(self):
        self.rest = factories.RestaurantFactory()
        self.dish1 = factories.MenuFactory(id_rest=self.rest)
        self.dish2 = factories.MenuFactory(id_rest=self.rest)
        self.dish3 = factories.MenuFactory(id_rest=self.rest)
        self.user = factories.UserFactory()
        self.order = factories.OrderFactory(id_rest=self.rest, dishes=(self.dish1, self.dish2, self.dish3))


    def test_get_rest_list(self):
        url = reverse('food_delivery:rests')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['rests'].count(),models.Restaurant.objects.count())

    def test_get_menu_detail(self):
        url = reverse('food_delivery:rest_menu', kwargs={'pk':self.rest.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.dish1.name)

    def test_post_order_update(self):
        url = reverse('food_delivery:update_order', kwargs={'pk': self.order.pk})
        dishes = self.order.dishes.all()
        dish_ids = [dish.pk for dish in dishes]
        data_post = {
            'first_name': self.order.id_user.first_name,
            'surname': self.order.id_user.surname,
            'address': self.order.id_user.address,
            'dishes': dish_ids,
            'promocode': self.order.promocode,
            'comment':'update_comment'

        }
        old_comment = self.order.comment
        response = self.client.post(url , data_post, follow = True)
        self.order.refresh_from_db()
        self.assertRedirects(response,reverse('food_delivery:orders_list')) # assertRedirects также проверяет статус код == 302
        self.assertNotEqual(old_comment,self.order.comment)

    def test_delete_order(self):
        url = reverse('food_delivery:delete_order',kwargs={'pk': self.order.pk})
        old_orders_count = models.Order.objects.count()
        response = self.client.delete(url)
        self.assertRedirects(response,reverse('food_delivery:orders_list'))
        self.assertGreater(old_orders_count,models.Order.objects.count())

    def test_create_order(self):
        url = reverse('food_delivery:create_order', kwargs={'pk': self.rest.pk})
        data_post = {
            'first_name': self.user.first_name,
            'surname': self.user.surname,
            'address': self.user.address,
            'dishes': [self.dish1.pk, self.dish2.pk],
            'promocode': 'ITCODECOOL',
            'comment': 'Base comment'
        }

        old_orders_count = models.Order.objects.count()
        response = self.client.post(url,data_post,follow=True)

        self.assertRedirects(response,reverse('food_delivery:rests'))
        self.assertGreater(models.Order.objects.count(),old_orders_count)



