# Generated by Django 4.2.4 on 2023-09-18 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_remove_orderupdatelog_user_delete_totalamount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalAmount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.customerprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='PayPalWebhookEvent',
        ),
    ]
