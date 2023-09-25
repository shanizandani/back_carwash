# Generated by Django 4.2.4 on 2023-09-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_remove_order_user_customerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='item_names',
            field=models.TextField(blank=True, null=True),
        ),
    ]