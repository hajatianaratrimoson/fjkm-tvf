from django.contrib import admin
from mpandraharaha.models import Mpiangona, Mpandray, Ankohonana
from django.contrib.auth.admin import UserAdmin


# class ProductImamgesAdmin(admin.TabularInline):
#     model = ProductImages
class MpiangonaAdminInline(admin.StackedInline):
    
    model = Mpiangona
    fields = ['name', 'surname']
    radio_fields = {"ankohonana": admin.HORIZONTAL}
    
    
    
    
class MpiangonaAdmin(admin.ModelAdmin):
    exclude=['piid']
    
    list_display = ['name', 'surname', 'ankohonana']
    list_select_related = ['ankohonana']
    #Activate search field on model
    search_fields = ['name', 'surname', 'ankohonana__anarana']

class MpandrayAdmin(admin.ModelAdmin):
    exclude = ['paid']
    list_display = ['karatra','mpiangona', 'taona', 'fiangonana' ]
    #Activate search field on model
    search_fields = ['karatra', 'mpiangona__name', 'mpiangona__surname']


class AnkohonanaAdmin(admin.ModelAdmin):
    inlines = [MpiangonaAdminInline]
    exclude=['ankid']
    list_display = ['anarana','faritra']
    #Activate search field on model 
    search_fields = ['anarana', 'faritra']

    
    

admin.site.register(Mpandray, MpandrayAdmin)
admin.site.register(Ankohonana, AnkohonanaAdmin)
admin.site.register(Mpiangona, MpiangonaAdmin)


