from django.contrib import admin

# Register your models here.
from .models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['gname','gprice','gcatalog','gshort_details','glong_details','gpub_time']
    list_filter = ['gcatalog','gvocation','gpub_time']
    search_fields = ['gname',]
    list_per_page = 20

admin.site.register(Goods,GoodsAdmin)