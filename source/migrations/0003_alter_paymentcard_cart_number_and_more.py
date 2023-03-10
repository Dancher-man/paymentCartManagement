# Generated by Django 4.1.4 on 2022-12-26 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0002_alter_paymentcard_cart_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentcard',
            name='cart_number',
            field=models.BigIntegerField(blank=True, default=4399802634517451, null=True, verbose_name='Номер карты'),
        ),
        migrations.AlterField(
            model_name='paymentcard',
            name='cart_sum',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='paymentcard',
            name='end_date_card_activity',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 18, 14, 43, 13, 943955), null=True, verbose_name='дата окончания активности карты'),
        ),
    ]
