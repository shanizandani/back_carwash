# Generated by Django 4.2.4 on 2023-09-13 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_order_customer_name_order_item_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_payment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
