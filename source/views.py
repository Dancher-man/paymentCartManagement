from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from source.models import PaymentCard


# Create your views here.


def check_status_view():
    count = 0
    check_status_cart = PaymentCard.objects.filter(end_date_card_activity__lte=datetime.now() + timedelta(days=30 * 20))

    if check_status_cart:
        cart_bulk_update_list = []
        count = check_status_cart.count()
        print(count)
        for cart in check_status_cart:
            cart.cart_status = PaymentCard.OVERDUE
            cart_bulk_update_list.append(cart)

        PaymentCard.objects.bulk_update(cart_bulk_update_list, ['cart_status'])
    context = {
        'count': count,
    }
    return context