# Generated by Django 4.1 on 2024-03-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]