# Generated by Django 4.0.6 on 2023-09-07 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_remove_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='purchase_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]