# Generated by Django 4.2.5 on 2023-10-22 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_recipe_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]