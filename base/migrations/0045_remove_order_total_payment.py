# Generated by Django 4.2.4 on 2023-09-18 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0044_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_payment',
        ),
    ]
