# Generated by Django 4.1.4 on 2022-12-26 08:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owners_name', models.CharField(max_length=255, verbose_name='Имя владельца карты')),
                ('cart_number', models.BigIntegerField(verbose_name='Номер карты')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата выпуска карты')),
                ('end_date_card_activity', models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 18, 8, 20, 46, 868669), null=True, verbose_name='дата окончания активности карты')),
                ('cart_sum', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Сумма')),
                ('cart_status', models.CharField(choices=[('activated', 'Активирована'), ('not_activated', 'не активирована'), ('overdue', 'просрочена')], max_length=40, verbose_name='Статус карты')),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('purchase_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость товара')),
                ('cart_numbers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='namer_cart', to='source.paymentcard')),
            ],
        ),
    ]
