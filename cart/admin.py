from django.contrib import admin
from cart.models import Cart,Order,Account,Orders,Payment
# Register your models here.

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Account)
admin.site.register(Orders)
admin.site.register(Payment)