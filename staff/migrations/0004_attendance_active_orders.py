# Generated by Django 4.1 on 2024-03-17 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_attendance_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='active_orders',
            field=models.IntegerField(default=0),
        ),
    ]