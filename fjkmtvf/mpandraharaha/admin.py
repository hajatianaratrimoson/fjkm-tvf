from django.contrib import admin
from mpandraharaha.models import Mpiangona, Mpandray, Ankohonana


# class ProductImamgesAdmin(admin.TabularInline):
#     model = ProductImages

class MpiangonaAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'ankohonana']
    list_select_related = ['ankohonana']
    search_fields = ['name', 'surname', 'ankohonana__anarana']

class MpandrayAdmin(admin.ModelAdmin):
    list_display = ['karatra','mpiangona', 'taona', 'fiangonana' ]
    search_fields = ['karatra', 'mpiangona__name', 'mpiangona__surname']


class AnkohonanaAdmin(admin.ModelAdmin):
    list_display = ['anarana','faritra']
    search_fields = ['anarana', 'faritra']

    
    
admin.site.register(Mpiangona, MpiangonaAdmin)
admin.site.register(Mpandray, MpandrayAdmin)
admin.site.register(Ankohonana, AnkohonanaAdmin)
