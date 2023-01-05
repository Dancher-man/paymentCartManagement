from django.contrib import admin

from source.models import PaymentCard, Purchases
from source.views import check_status_view

"""!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer


class PurchaseInline(admin.TabularInline):
    model = Purchases
    extra = 0


@admin.register(PaymentCard)
class PaymentCardAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ('owners_name', 'cart_number', 'created_at', 'end_date_card_activity', 'cart_status')
    list_display_links = ('owners_name',)
    list_filter = ('owners_name', 'cart_number', 'created_at', 'end_date_card_activity', 'cart_status')
    readonly_fields = ('end_date_card_activity', 'created_at')
    search_fields = ('owners_name', 'cart_number', 'created_at', 'end_date_card_activity', 'cart_status')
    inlines = [PurchaseInline]
    save_on_top = True
    save_as = True
    list_editable = ('cart_status',)

    @button(
            change_form=True,
            html_attrs={'style': 'background-color:#417690;color:#fff'})
    def change_cart_status(self, request):
        check_status = check_status_view()
        self.message_user(request, f"Изменено {check_status['count']} записей")
        return HttpResponseRedirectToReferrer(request)


@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'purchase_date', 'product_price', '_cart_number')
    list_display_links = ('product_name',)
    list_filter = ('product_name',)
    readonly_fields = ('purchase_date',)
    search_fields = ('product_name', 'purchase_date', 'cart_numbers__cart_number')
    save_on_top = True
    save_as = True

    def _cart_number(self, obj):
        return obj.cart_numbers.cart_number
