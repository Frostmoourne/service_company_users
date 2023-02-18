
from django.test import TestCase
from .models import Customer


class CustomerModelTest(TestCase):
    def test_create_customer(self):
        customer = Customer.objects.create(
            first_name='Иван',
            last_name='Иванов',
            email='ivan.ivanov@example.com',
            address='г. Тюмень, 1 улица Строителей',
            city='Тюмень',
            zip_code='625000'
        )
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(customer.first_name, 'Иван')
        self.assertEqual(customer.last_name, 'Иванов')
        self.assertEqual(customer.email, 'ivan.ivanov@example.com')
        self.assertEqual(customer.address, 'г. Тюмень, 1 улица Строителей')
        self.assertEqual(customer.city, 'Тюмень')
        self.assertEqual(customer.zip_code, '625000')

    def test_update_customer(self):
        customer = Customer.objects.create(
            first_name='Иван',
            last_name='Иванов',
            email='ivan.ivanov@example.com',
            address='г. Тюмень, 1 улица Строителей',
            city='Тюмень',
            zip_code='625000'
        )
        customer.first_name = 'Петр'
        customer.save()
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(customer.first_name, 'Петр')
        self.assertEqual(customer.last_name, 'Иванов')
        self.assertEqual(customer.email, 'ivan.ivanov@example.com')
        self.assertEqual(customer.address, 'г. Тюмень, 1 улица Строителей')
        self.assertEqual(customer.city, 'Тюмень')
        self.assertEqual(customer.zip_code, '625000')
