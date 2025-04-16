from django.contrib import admin
from mpandraharaha.models import Mpiangona, Mpandray,Ankohonana, Tossaafiko, Mpikambana, Batisa, Katekomena, Mariazy
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
    fields = ['anarana', 'fanampiny', 'toerana']
    # radio_fields = {"ankohonana": admin.HORIZONTAL}
    
class MpikambanaAdminInline(admin.TabularInline):
    model = Mpikambana
    can_delete = False # ReadOnly
    extra = 0 # Reset Default Count = 3
    verbose_name =['Mpikambana'] # Rename Tab Title
    verbose_name_plural = "Tossaafiko" # Plural rename tab Title
    readonly_fields = ['mpikambana','tossaafiko', 'andraikitra', 'taona'] # ReadOnly
    # general_tab = "ankohonana"
    fields = ['mpikambana','tossaafiko', 'andraikitra', 'taona']
    # radio_fields = {"ankohonana": admin.HORIZONTAL}

class MpandrayAdminInline(admin.TabularInline):
    model = Mpandray
    can_delete = False # ReadOnly
    extra = 0 # Reset Default Count = 3
    verbose_name =['Mpandray'] # Rename Tab Title
    verbose_name_plural = "Mpandray" # Plural rename tab Title
    readonly_fields = ['karatra','taona', 'fiangonana'] # ReadOnly
    # general_tab = "ankohonana"
    fields = ['karatra','taona', 'fiangonana']

class BatisaAdminInline(admin.TabularInline):
    model = Batisa
    can_delete = False # ReadOnly
    extra = 0 # Reset Default Count = 3
    verbose_name =['Batisa'] # Rename Tab Title
    verbose_name_plural = "Batisa" # Plural rename tab Title
    readonly_fields = ['daty_nanolorana','daty_batisa', 'rad', 'fiangonana', 'firenena'] # ReadOnly
    # general_tab = "ankohonana"
    fields = ['daty_nanolorana','daty_batisa', 'rad', 'fiangonana', 'firenena']

class KatekomenaAdminInline(admin.TabularInline):
    model = Katekomena
    can_delete = False # ReadOnly
    extra = 0 # Reset Default Count = 3
    verbose_name =['Katekomena'] # Rename Tab Title
    verbose_name_plural = "Katekomena" # Plural rename tab Title
    readonly_fields = ['anarana','andiany', 'daty_nidirana','sata', 'daty_nivoahana', 'fiangonana', 'firenena'] # ReadOnly
    # general_tab = "ankohonana"
    fields = ['anarana','andiany', 'daty_nidirana','sata','daty_nivoahana', 'fiangonana', 'firenena']


class MpiangonaResource(resources.ModelResource):
    class Meta:
        model = Mpiangona
        # List related field by ForeigKey
        fields = ['anarana', 'fanampiny', 'adiresy', 'finday','ankohonana__anarana','toerana', 'zanaka']

@admin.register(Mpiangona)
class MpiangonaAdmin(ImportExportModelAdmin):
    resource_classes = [MpiangonaResource]
    inlines = [BatisaAdminInline,KatekomenaAdminInline, MpandrayAdminInline, MpikambanaAdminInline ]
    
    # exclude=['piid']
    list_display = ['anarana', 'fanampiny', 'anarana_zatovo','ankohonana']
    list_select_related = ['ankohonana']
    list_filter = ['ankohonana', 'ankohonana__faritra']
    
    #Activate search field on model
    search_fields = ['anarana', 'fanampiny', 'ankohonana__anarana', 'anarana_zatovo']


class MpandrayResource(resources.ModelResource):
    class Meta:
        model: Mpandray
        fields = ['karatra','mpandray__anarana', 'mpandray__fanampiny', ]

@admin.register(Mpandray)
class MpandrayAdmin(ImportExportModelAdmin):
    # exclude = ['paid']
    resource_classes = [MpandrayResource]
    list_display = ['karatra','mpandray']
    list_filter = ['karatra', 'mpandray', 'taona', 'fiangonana']


class MpikambanaResource(resources.ModelResource):
    class Meta:
        model = Mpikambana
        fields = ('mpikambana__anarana', 'mpikambana__fanampiny', 'tossaafiko__anarana', 'andraikitra', 'taona')

@admin.register(Mpikambana)
class MpikambanaAdmin(ImportExportModelAdmin):
    resource_classes = [MpikambanaResource]
    list_display = ['tossaafiko', 'mpikambana', 'andraikitra', 'taona']
    # search_fields = ['tossaafiko', 'mpiangona']
    list_filter = ['tossaafiko', 'mpikambana', 'andraikitra', 'taona']
     
     

class AnkohonanaResource(resources.ModelResource):
    class Meta:
        model = Ankohonana
        fields = ['anarana', 'faritra']  

@admin.register(Ankohonana) 
class AnkohonanaAdmin(ImportExportModelAdmin):
    resource_classes = [AnkohonanaResource]
    inlines = [MpiangonaAdminInline]
    #exclude field mentionned
    # exclude=['ankid']
    list_display = ['anarana','faritra_tvf', 'fokotany', 'faritra', 'firenena']
    #Activate search field on model 
    # search_fields = ['anarana', 'faritra']
    list_filter = ['anarana','faritra_tvf', 'fokotany', 'faritra', 'firenena']


class TossaafikoResource(resources.ModelResource):
    class Meta:
        model = Tossaafiko
        fields = ['anarana', 'fanamarihana']


@admin.register(Tossaafiko)
class TossaafikoAdmin(ImportExportModelAdmin):
    resource_classes = [TossaafikoResource]
    # exclude = ['said']
    list_display = ['anarana', 'fanamarihana']
    
    #Activate search field on model
    search_fields = ['anarana']


class BatisaResource(resources.ModelResource):
    class Meta:
        model = Batisa
        fields = ('anarana__anarana', 'anarana_fanampy', 'daty_nanolorana', 'daty_batisa')

@admin.register(Batisa)
class BatisaAdmin(ImportExportModelAdmin):
    resource_classes = [BatisaResource]
    list_display = ['anarana', 'daty_nanolorana', 'daty_batisa']
    search_fields = ['anarana__anarana', 'anarana__fanampiny', 'daty_nanolorana', 'daty_batisa']


class KatekomenaResource(resources.ModelResource):
    class Meta:
        model: Katekomena
        fields = ['anarana','daty_nidirana','sata','daty_nivoahana', 'andiany','fiangonana', 'firenena' ]

@admin.register(Katekomena)
class KatekomenaAdmin(ImportExportModelAdmin):
    # exclude = ['paid']
    resource_classes = [KatekomenaResource]
    list_display = ['anarana','daty_nidirana','sata','daty_nivoahana', 'andiany','fiangonana', 'firenena' ]
    search_fields = ['anarana','daty_nidirana','sata','daty_nivoahana', 'andiany','fiangonana', 'firenena' ]
    list_filter = ['anarana', 'andiany','sata','fiangonana', 'firenena' ]



class MariazyResource(resources.ModelResource):
    class Meta:
        model: Mariazy
        # fields = ['lahy','vavy','sata','daty_nivoahana', 'andiany','fiangonana', 'firenena' ]

@admin.register(Mariazy)
class MariazyaAdmin(ImportExportModelAdmin):
    # exclude = ['paid']
    resource_classes = [MariazyResource]
    list_display = ['lahy','vavy','daty_sivily','kaominina','daty_fiangonana', 'fiangonana', 'firenena' ]
    search_fields = ['lahy','vavy','daty_sivily','kaominina','daty_fiangonana', 'fiangonana', 'firenena' ]
    list_filter = ['lahy','vavy','kaominina', 'fiangonana', 'firenena' ]
# admin.site.register(Ankohonana, AnkohonanaAdmin)

