# Generated by Django 4.2.5 on 2023-12-02 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_reply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-date']},
        ),
    ]