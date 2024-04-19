from django.contrib import admin

from myrecipes.models import Recipe, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'category', 'description', 'image']


admin.site.register(Recipe, ProductAdmin)
admin.site.register(Category)
