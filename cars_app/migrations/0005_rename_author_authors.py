# Generated by Django 5.1.3 on 2024-12-04 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_app', '0004_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Authors',
        ),
    ]
