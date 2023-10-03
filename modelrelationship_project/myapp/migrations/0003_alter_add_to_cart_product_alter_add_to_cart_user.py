# Generated by Django 4.2.5 on 2023-10-03 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_alter_add_to_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_to_cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product'),
        ),
        migrations.AlterField(
            model_name='add_to_cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]