from django.contrib import admin
from .models import Product,offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','stock']


class OfferAdmin(admin.ModelAdmin):
    list_display = ['code','discount']



admin.site.register(offer,OfferAdmin)

admin.site.register(Product,ProductAdmin)
admin.site.site_header='Ahmad'
admin.site.site_title='Ahmad'