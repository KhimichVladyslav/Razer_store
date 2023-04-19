from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self) -> None:
        self.data = Category.objects.create(name='mouse', slug='mouse')

    def test_category_model_entry(self):
        data = self.data
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry_1(self):
        data = self.data
        self.assertEqual(str(data), 'mouse')


class TestProductsModel(TestCase):

    def setUp(self) -> None:
        Category.objects.create(name='mouse', slug='mouse')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='Razer Viper', created_by_id=1, slug='razer-viper',
                                           price='3999', image='viper')

    def test_product_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertTrue(str(data), 'Razer Viper')
