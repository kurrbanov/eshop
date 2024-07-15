# Generated by Django 5.0.4 on 2024-07-04 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'verbose_name': 'Свойство', 'verbose_name_plural': 'Свойства'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Фото товара', 'verbose_name_plural': 'Фото товаров'},
        ),
        migrations.AlterField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(to='shop.attribute', verbose_name='Свойства'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(verbose_name='В наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Товар'),
        ),
    ]