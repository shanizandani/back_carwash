# Generated by Django 4.2.4 on 2023-09-13 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0023_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(max_length=254)),
                ('product_name', models.CharField(max_length=100)),
                ('washing_amount', models.PositiveIntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
