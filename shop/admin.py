from django.contrib import admin
from .models import Product, Order


admin.site.site_header = "Men's Accessories"
admin.site.site_title = "Jimmy's Shop"
admin.site.index_title = "Shop for best prices"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')
    
    change_category_to_default.short_description = "Default Category"
    list_display = ('title', 'price', 'discount_price', 'category', 'description', 'image')
    search_fields = ('title', 'category',)
    actions = ("change_category_to_default",)
    list_editable = ("price", "category")

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)