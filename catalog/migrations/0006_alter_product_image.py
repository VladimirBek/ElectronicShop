# Generated by Django 4.2.4 on 2023-08-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_userdata_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='изображение (превью)'),
        ),
    ]
