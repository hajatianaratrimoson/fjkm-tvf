from django.contrib import admin
from mpandraharaha.models import Mpiangona, Mpandray,Ankohonana, Tossaafiko, Mpikambana
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields


"""
ForeignKey Tab list vew
"""
class MpiangonaAdminInline(admin.TabularInline):
    model = Mpiangona
    can_delete = False # ReadOnly
    extra = 0 # Reset Default Count = 3
    verbose_name =['Ankohonana','Iray Trano'] # Rename Tab Title
    verbose_name_plural = "Iray Trano" # Plural rename tab Title
    readonly_fields = ['anarana', 'fanampiny', 'toerana'] # ReadOnly
    # general_tab = "ankohonana"
    # fields = ['anarana', 'fanampiny', 'toerana']
    # radio_fields = {"ankohonana": admin.HORIZONTAL}

class MpiangonaResource(resources.ModelResource):
    class Meta:
        model = Mpiangona
        # List related field by ForeigKey
        # fields = ['anarana', 'fanampiny', 'adiresy', 'finday','ankohonana__anarana','toerana', 'zanaka']

@admin.register(Mpiangona)
class MpiangonaAdmin(ImportExportModelAdmin):
    resource_classes = [MpiangonaResource]
    # exclude=['piid']
    list_display = ['anarana', 'fanampiny', 'anarana_zatovo','ankohonana']
    list_select_related = ['ankohonana']
    list_filter = ['ankohonana', 'ankohonana__faritra']
    
    #Activate search field on model
    search_fields = ['anarana', 'fanampiny', 'ankohonana__anarana', 'anarana_zatovo']


class MpandrayResource(resources.ModelResource):
    class Meta:
        model: Mpandray
        fields = ['karatra','mpiangona__anarana', 'mpiangona__fanampiny', ]

@admin.register(Mpandray)
class MpandrayAdmin(ImportExportModelAdmin):
    # exclude = ['paid']
    resource_classes = [MpandrayResource]
    list_display = ['karatra','mpiangona']
    list_filter = ['karatra', 'mpiangona', 'taona', 'fiangonana']


class MpikambanaResource(resources.ModelResource):
    class Meta:
        model = Mpikambana
        # fields = ('mpiangona__anarana', 'mpiangona__fanampiny', 'tossaafiko__anarana', 'andraikitra',)

@admin.register(Mpikambana)
class MpikambanaAdmin(ImportExportModelAdmin):
    resource_classes = [MpikambanaResource]
    list_display = ['tossaafiko', 'mpiangona', 'andraikitra']
    # search_fields = ['tossaafiko', 'mpiangona']
    list_filter = ['tossaafiko', 'mpiangona', 'andraikitra']
     
     

class AnkohonanaResource(resources.ModelResource):
    class Meta:
        model = Ankohonana
        # fields = ['anarana', 'faritra']  

@admin.register(Ankohonana) 
class AnkohonanaAdmin(ImportExportModelAdmin):
    resource_classes = [AnkohonanaResource]
    inlines = [MpiangonaAdminInline]
    #exclude field mentionned
    # exclude=['ankid']
    list_display = ['anarana','faritra']
    #Activate search field on model 
    # search_fields = ['anarana', 'faritra']
    list_filter = ['anarana', 'faritra']


class TossaafikoResource(resources.ModelResource):
    class Meta:
        model = Tossaafiko
        # fields = ['anarana', 'fanamarihana']


@admin.register(Tossaafiko)
class TossaafikoAdmin(ImportExportModelAdmin):
    resource_classes = [TossaafikoResource]
    # exclude = ['said']
    list_display = ['anarana', 'fanamarihana']
    
    #Activate search field on model
    search_fields = ['anarana']

    
    
# admin.site.register(Ankohonana, AnkohonanaAdmin)

