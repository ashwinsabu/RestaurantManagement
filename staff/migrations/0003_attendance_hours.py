# Generated by Django 4.1 on 2024-03-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_rename_login_time_attendance_login_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='hours',
            field=models.IntegerField(null=True),
        ),
    ]
