from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.register(Product)


class ProductInLine(admin.StackedInline):
    model = Product
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInLine]
