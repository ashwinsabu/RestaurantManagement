# Generated by Django 4.1 on 2024-03-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_customerrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
