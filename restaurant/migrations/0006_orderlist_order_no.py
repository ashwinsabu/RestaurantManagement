# Generated by Django 4.1 on 2024-03-09 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_remove_orders_menu_no_orderlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='order_no',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.orders'),
        ),
    ]
