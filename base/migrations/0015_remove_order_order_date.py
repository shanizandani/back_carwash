# Generated by Django 4.0.6 on 2023-09-07 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_order_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
    ]
