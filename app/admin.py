from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    ist_display = ('address', 'whatsapp_number', 'phone_number')
    search_fields = ('address', 'whatsapp_number', 'phone_number')




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'description', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px;"/>'.format(obj.image.url))
        return "-"
    image_tag.short_description = 'Image'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_tag', 'price', 'available', 'created_at')
    list_filter = ('category', 'available')
    search_fields = ('name', 'category__name')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px;"/>'.format(obj.image.url))
        return "-"
    image_tag.short_description = 'Image'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)