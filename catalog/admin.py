from django.contrib import admin

from catalog.models import Product, Category, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit_price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'ind_number', 'country',)
    list_filter = ('country',)
    search_fields = ('ind_number',)
