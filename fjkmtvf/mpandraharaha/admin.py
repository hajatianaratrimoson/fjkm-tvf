from django.contrib import admin
from mpandraharaha.models import Mpiangona, Mpandray,Ankohonana, Tossaafiko, Mpikambana
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields
# class ProductImamgesAdmin(admin.TabularInline):
#     model = ProductImages
class MpiangonaAdminInline(admin.TabularInline):
    
    model = Mpiangona
    can_delete = False
    extra = 0
    verbose_name =['Ankohonana','Iray Trano']
    verbose_name_plural = "Iray Trano"
    readonly_fields = ['name', 'surname', 'toerana']
    general_tab = "ankohonana"
    fields = ['name', 'surname', 'toerana']
    # radio_fields = {"ankohonana": admin.HORIZONTAL}

class MpiangonaResource(resources.ModelResource):
    class Meta:
        model = Mpiangona
        fields = ['name', 'surname', 'adress', 'contact','ankohonana__anarana','toerana', 'zanaka']

@admin.register(Mpiangona)
class MpiangonaAdmin(ImportExportModelAdmin):
    resource_classes = [MpiangonaResource]
    exclude=['piid']
    list_display = ['name', 'surname', 'ankohonana']
    list_select_related = ['ankohonana']
    list_filter = ['ankohonana', 'ankohonana__faritra']
    
    #Activate search field on model
    search_fields = ['name', 'surname', 'ankohonana__anarana']


class MpandrayRessource(resources.ModelResource):
    class Meta:
        model: Mpandray
        fields = ['karatra','mpandray_mpiangona__name', 'mpandray_mpiangona__surname', ]
@admin.register(Mpandray)
class MpandrayAdmin(ImportExportModelAdmin):
    resource_classes = [MpandrayRessource]
    # fields = ['mpiangona__name']
    list_display = ['karatra','mpandray_mpiangona']
    list_filter = ['karatra', 'mpandray_mpiangona', 'taona', 'fiangonana']


class MpikambanaResource(resources.ModelResource):
    class Meta:
        model = Mpikambana
        fields = ('mpiangona__name', 'mpiangona__surname', 'tossaafiko__anarana', 'andraikitra',)

@admin.register(Mpikambana)
class MpikambanaAdmin(ImportExportModelAdmin):
    resource_classes = [MpikambanaResource]
    list_display = ['tossaafiko', 'mpiangona', 'andraikitra']
    # search_fields = ['tossaafiko', 'mpiangona']
    list_filter = ['tossaafiko', 'mpiangona', 'andraikitra']
        
class AnkohonanaAdmin(ImportExportModelAdmin):
    model = Ankohonana
    inlines = [MpiangonaAdminInline]
    #exclude field mentionned
    exclude=['ankid']
    list_display = ['anarana','faritra']
    #Activate search field on model 
    search_fields = ['anarana', 'faritra']
    list_filter = ['faritra']

class TossaafikoAdmin(ImportExportModelAdmin):
    model = Tossaafiko
    list_display = ['anarana', 'fanamarihana']
    
    #Activate search field on model
    search_fields = ['anarana']

    
    
admin.site.register(Ankohonana, AnkohonanaAdmin)
admin.site.register(Tossaafiko, TossaafikoAdmin)

