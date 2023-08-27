from django.utils.timezone import now

from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_price = models.IntegerField(verbose_name='цена за покупку')
    produce_day = models.DateField(verbose_name='дата создания')
    last_change = models.DateField(verbose_name='дата последнего изменения', default=now)

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contacts(models.Model):
    country = models.CharField(max_length=50, verbose_name='страна')
    ind_number = models.CharField(max_length=10, verbose_name='ИНН')
    address = models.TextField(verbose_name='адрес', **NULLABLE)

    def __str__(self):
        return f'{self.country} {self.address}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class UserData(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    phone_number = models.CharField(max_length=50, verbose_name='телефон')
    message = models.TextField(verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.message}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Version(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'активна'
        NOT_ACTIVE = 'не активна'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.CharField(max_length=50, verbose_name='номер версии')
    name = models.CharField(max_length=100, verbose_name='название версии')
    status = models.CharField(max_length=15, choices=Status.choices, verbose_name='признак версии')

    def __str__(self):
        return f'версия {self.product.name} номер {self.number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
