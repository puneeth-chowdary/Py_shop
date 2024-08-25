from django.contrib import admin
from .models import Product,offer,carty,check
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')
class offerAdmin(admin.ModelAdmin):
    list_display=('code','discount')
class cartyAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')
class checkAdmin(admin.ModelAdmin):
    list_display=('name','mail','phone_number','address')

admin.site.register(Product,ProductAdmin)
admin.site.register(offer,offerAdmin)
admin.site.register(carty,cartyAdmin)
admin.site.register(check,checkAdmin)