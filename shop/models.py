import uuid

from django.contrib.auth.models import User
from django.db import models


class ProductManager(models.Manager):
    def in_stock(self):
        return self.get_queryset().filter(stock__gt=0)


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    stock = models.IntegerField(verbose_name="В наличии")
    attributes = models.ManyToManyField('Attribute', verbose_name="Свойства")

    objects = ProductManager()

    def __str__(self):
        return f"{self.title}: #{self.id}"

    class Meta:
        db_table = 'product'
        indexes = [models.Index(fields=['title'])]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    image = models.ImageField(verbose_name="Изображение")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")

    class Meta:
        verbose_name = "Фото товара"
        verbose_name_plural = "Фото товаров"


class Attribute(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Свойство"
        verbose_name_plural = "Свойства"


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
