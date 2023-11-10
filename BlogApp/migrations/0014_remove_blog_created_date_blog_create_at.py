# Generated by Django 4.2.6 on 2023-11-04 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0013_alter_blog_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_date',
        ),
        migrations.AddField(
            model_name='blog',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]