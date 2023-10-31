# Generated by Django 4.2.5 on 2023-10-19 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curd_model',
            name='roll_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='curd_model',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]