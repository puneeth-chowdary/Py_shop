# Generated by Django 5.0.6 on 2024-08-21 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_delete'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='delete',
            new_name='remove',
        ),
    ]
