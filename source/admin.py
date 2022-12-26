from datetime import datetime

from django.contrib import admin
from django.db.models import QuerySet

from source.models import PaymentCard, Purchases


class PurchaseInline(admin.TabularInline):
    model = Purchases
    extra = 1
    readonly_fields = ('product_name', 'purchase_date', 'product_price', 'cart_numbers')


@admin.register(PaymentCard)
class PaymentCardAdmin(admin.ModelAdmin):
    list_display = ('owners_name', 'cart_number', 'created_at', 'end_date_card_activity', 'cart_status')
    list_display_links = ('owners_name',)
    list_filter = ('owners_name', 'cart_number', 'created_at', 'end_date_card_activity', 'cart_status')
    readonly_fields = ('end_date_card_activity', 'created_at')
    search_fields = ('owners_name', 'cart_number', 'created_at', 'end_date_card_activity', 'cart_status')
    inlines = [PurchaseInline]
    save_on_top = True
    save_as = True
    list_editable = ('cart_status',)
    actions = ['check_status_activ']

    @admin.action(description='Проверить дату активации')
    def check_status_activ(self, request, qs: QuerySet):
        if qs.filter(end_date_card_activity__lte=datetime.now()):
            qs.update(cart_status=PaymentCard.OVERDUE)


@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'purchase_date', 'product_price', '_cart_number')
    list_display_links = ('product_name',)
    list_filter = ('product_name',)
    readonly_fields = ('purchase_date', 'cart_numbers')
    search_fields = ('product_name', 'purchase_date', 'cart_numbers__cart_number')
    save_on_top = True
    save_as = True

    def _cart_number(self, obj):
        return obj.cart_numbers.cart_number
