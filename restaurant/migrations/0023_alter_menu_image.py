# Generated by Django 4.1 on 2024-04-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0022_alter_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/test/'),
        ),
    ]
