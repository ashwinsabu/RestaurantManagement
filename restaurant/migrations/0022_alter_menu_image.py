# Generated by Django 4.1 on 2024-04-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0021_orders_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='uploads/test/'),
        ),
    ]