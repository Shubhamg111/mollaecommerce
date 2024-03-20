from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug', 'total_products']
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display=['category','name','price','quantity','isAvailable']
    list_editable=['price','quantity','isAvailable']
    prepopulated_fields= {'slug': ('name',)}
    inlines=[ProductImageInline]


@admin.register(Banner)
class AdminBanner(admin.ModelAdmin):
    list_display=['name','is_active','get_image']
    list_editable=["is_active"]

    def get_image(self, obj):
        if  obj.image:
            return format_html('<img src="{}" width="150" height="80"/>',obj.image.url)
        else:
            return "No Image"
        


@admin.register(Settings)
class AdminSettings(admin.ModelAdmin):
    list_display=['name','email','address','phone','clogo']
    list_editable=['address','phone']

   
    def clogo(self, obj):
        return format_html('<img src="{}" width="70" height="40"/>',obj.logo.url)
       