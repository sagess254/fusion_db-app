from django.contrib import admin

from myapp.models import Product

admin.site.site_title="GID Shop"
admin.site.site_header="Shop MIS"
admin.site.index_title="Shop MIS Admin"


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount', 'created_at', 'for_sale')
    search_fields = ('name','code','category')
    list_filter = ('category','for_sale')
    ordering = ('name','-price')
