from ast import Delete
from email.policy import default
from tabnanny import verbose
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models
from phone_field import PhoneField

class Author(models.Model):  #наследование
    name = models.CharField(max_length=100, blank=False, )
    email = models.EmailField(blank =False, primary_key=True)


class Comment(models.Model):  #наследование
    title = models.CharField(max_length=100, verbose_name='Комментарий')
    #subtitle = models.CharField(max_length=300)
    content = models.TextField(blank=False, verbose_name='Содержание комментария')
    image = models.ImageField(blank=True, upload_to='uploads', verbose_name='Фото') ## чтобы картинку вставлять не обязательно то blank=True
    date_of_creation = models.DateTimeField(verbose_name='Дата создания комментария')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)


class Order(models.Model):  #наследование
    order_adress = models.CharField(max_length=300, verbose_name='Адрес доставки')
    order_tel = PhoneField(blank=True, help_text='Введите свой номер телефона в формате +375-XX-XXX-XX-XX', verbose_name='Телефон', default=0)
    order_description = models.TextField(blank=False, verbose_name='Пожелания по доставке')
    date_of_order = models.DateTimeField(verbose_name='Дата заказа')
    order_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена услуги', default=0)

    ORDER_TYPE = [
        ("NS", "Нет слов"), ("NM", "Не мелочи"), ("SN", "Срочно надо"), ("PV", "Почтенный возраст"), ("PR", "По рукам")
    ]
    order_type = models.CharField(choices=ORDER_TYPE, max_length=2, default='NM', verbose_name='Тип заказа')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.order_adress;