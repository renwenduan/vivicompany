from django.contrib import admin

# Register your models here.
from .models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['gname','gprice','gmain_catalog','gsales','gvocation']
    list_filter = ['gmain_catalog','gvocation']
    search_fields = ['gname']
    list_per_page = 20

admin.site.register(Goods,GoodsAdmin)