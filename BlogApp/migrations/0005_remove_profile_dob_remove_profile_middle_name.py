# Generated by Django 4.2.6 on 2023-10-31 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_profile_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='middle_name',
        ),
    ]
