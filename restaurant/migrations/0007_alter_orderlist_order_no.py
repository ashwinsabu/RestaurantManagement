# Generated by Django 4.1 on 2024-03-09 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_orderlist_order_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='order_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.orders'),
        ),
    ]