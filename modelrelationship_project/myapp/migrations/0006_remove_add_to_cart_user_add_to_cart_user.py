# Generated by Django 4.2.5 on 2023-10-03 14:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_remove_add_to_cart_product_remove_add_to_cart_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_to_cart',
            name='user',
        ),
        migrations.AddField(
            model_name='add_to_cart',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
