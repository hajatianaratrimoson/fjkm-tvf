from django.contrib import admin
from mpandraharaha.models import Mpiangona


# class ProductImamgesAdmin(admin.TabularInline):
#     model = ProductImages

class MpiangonaAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


admin.site.register(Mpiangona, MpiangonaAdmin)
