# Generated by Django 5.0 on 2024-02-13 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_history_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='car',
        ),
    ]
