# Generated by Django 4.0.6 on 2023-08-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_order_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='product_photos/default-photo-filename.jpg', upload_to='product_photos/'),
        ),
    ]