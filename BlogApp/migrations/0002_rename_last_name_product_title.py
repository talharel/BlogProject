# Generated by Django 4.2.6 on 2023-10-31 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='last_name',
            new_name='Title',
        ),
    ]
