# Generated by Django 5.0.3 on 2024-03-15 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
