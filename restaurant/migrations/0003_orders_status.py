# Generated by Django 4.1 on 2024-03-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_quantity_menu_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]