import random

from django.db import models
from datetime import timedelta, datetime


class PaymentCard(models.Model):
    ACT = 'activated'
    OVERDUE = 'overdue'
    NOT_ACT = 'not_activated'

    CART_STATUS = [(ACT, 'Активирована'), (NOT_ACT, 'не активирована'), (OVERDUE, 'просрочена')]
    owners_name = models.CharField(max_length=255, verbose_name='Имя владельца карты')
    cart_number = models.BigIntegerField(verbose_name='Номер карты', blank=True, null=True,
                                         default=int(random.uniform(4000000000000000, 4900000000000000)))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата выпуска карты')
    end_date_card_activity = models.DateTimeField(verbose_name='дата окончания активности карты', blank=True, null=True,
                                                  default=datetime.now() + timedelta(days=30 * 18))
    cart_sum = models.DecimalField(verbose_name='Сумма', max_digits=10, decimal_places=2)
    cart_status = models.CharField(max_length=40, choices=CART_STATUS, verbose_name='Статус карты')

    def __str__(self):
        return self.owners_name

    class Meta:
        db_table = 'payment_cart'
        verbose_name = 'Платежная карта'
        verbose_name_plural = 'Платежные карты'
        ordering = ['-created_at']


class Purchases(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='Наименование товара')
    purchase_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')
    product_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Стоимость товара')
    cart_numbers = models.ForeignKey('source.PaymentCard', on_delete=models.CASCADE, related_name='cart_numbers',
                                     verbose_name='Номер карты')

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'purchases'
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        ordering = ['-purchase_date']
