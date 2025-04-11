from django.contrib import admin
from tetibola.models import Rafitra, Kaonty, Laminasa, Diarimbola, Ded
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
# from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields



class RafitraResource(resources.ModelResource):
    class Meta:
        model = Rafitra
        # fields = ['axe', 'fanamarihana']

@admin.register(Rafitra)
class RafitraAdmin(ImportExportModelAdmin):
    resource_classes = [RafitraResource]
    # inlines = [BatisaAdminInline,KatekomenaAdminInline, MpandrayAdminInline, MpikambanaAdminInline ]
    
    list_display = ['axe', 'fanamarihana']
    list_filter = ['axe', 'fanamarihana']
    
    #Activate search field on model
    search_fields = ['axe', 'fanamarihana']


class KaontyResource(resources.ModelResource):
    class Meta:
        model = Kaonty
        # fields = ['isa', 'anarana', 'rafitra__axe']

@admin.register(Kaonty)
class KaontyAdmin(ImportExportModelAdmin):
    resource_classes = [KaontyResource]
    
    list_display = ['isa', 'anarana', 'rafitra']
    list_filter = ['isa', 'anarana', 'rafitra']
    
    #Activate search field on model
    search_fields = ['isa', 'anarana', 'rafitra']


class LaminasaResource(resources.ModelResource):
    class Meta:
        model = Laminasa
        # fields = ['tossaafiko__anarana', 'daty', 'asa', 'toerana', 'fanamarihana']

@admin.register(Laminasa)
class LaminasaAdmin(ImportExportModelAdmin):
    resource_classes = [LaminasaResource]
    
    list_display = ['tossaafiko', 'daty', 'asa', 'toerana', 'fanamarihana']
    list_filter = ['tossaafiko', 'asa', 'toerana', 'fanamarihana']
    
    #Activate search field on model
    search_fields = ['tossaafiko', 'daty', 'asa', 'toerana', 'fanamarihana']
    

class DiarimbolaResource(resources.ModelResource):
    class Meta:
        model = Diarimbola
        # fields = [ 'kaonty', 'vola', 'fanamarihana']

@admin.register(Diarimbola)
class DiarimbolaAdmin(ImportExportModelAdmin):
    resource_classes = [DiarimbolaResource]
    
    list_display = ['kaonty','vola','fanamarihana']
    list_filter = ['kaonty',  'vola','fanamarihana']
    
    #Activate search field on model
    search_fields = ['kaonty', 'fanamarihana', 'vola']



class DedResource(resources.ModelResource):
    class Meta:
        model = Ded
        # fields = ['num_ded', 'daty_ded', 'tossaafiko', 'laminasa','diarimbola', 'fandaniana', 'sata']

@admin.register(Ded)
class DedAdmin(ImportExportModelAdmin):
    resource_classes = [DedResource]
    
    list_display = [ 'mpitantsorabola','num_ded', 'daty_ded', 'tossaafiko', 'laminasa','diarimbola', 'fandaniana', 'sata']
    list_filter = [ 'mpitantsorabola', 'num_ded', 'tossaafiko', 'laminasa','diarimbola', 'fandaniana', 'sata' ]
    
    #Activate search field on model
    search_fields = ['mpitantsorabola', 'num_ded', 'daty_ded', 'tossaafiko', 'laminasa','diarimbola', 'fandaniana', 'sata' ]