from datetime import datetime, timedelta

from source.models import PaymentCard


def check_status_view():
    count = 0
    check_status_cart = PaymentCard.objects.filter(end_date_card_activity__lte=datetime.now())

    if check_status_cart.count() > 0:
        cart_bulk_update_list = []
        count = check_status_cart.count()
        for cart in check_status_cart:
            cart.cart_status = PaymentCard.OVERDUE
            cart_bulk_update_list.append(cart)

        PaymentCard.objects.bulk_update(cart_bulk_update_list, ['cart_status'])
    context = {
        'count': count,
    }
    return context