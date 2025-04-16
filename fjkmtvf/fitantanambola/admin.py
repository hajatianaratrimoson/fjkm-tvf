from django.contrib import admin
from fitantanambola.models import Rafitra, Kaonty, Laminasa, Diarimbola, Ded
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
# from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user



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
class LaminasaAdmin(GuardedModelAdmin, ImportExportModelAdmin):
    # resource_classes = [LaminasaResource]
   
    list_display = ['tossaafiko', 'daty', 'asa', 'toerana', 'fanamarihana']
    list_filter = ['tossaafiko', 'asa', 'toerana', 'fanamarihana']
    
    #Activate search field on model
    search_fields = ['tossaafiko', 'daty', 'asa', 'toerana', 'fanamarihana']
    
    def has_module_permission(self, request):
        if super().has_module_permission(request):
            return True
        return self.get_model_objects(request).exists()
    
    def get_queryset(self, request):
        # return super().get_queryset(request)
        if request.user.is_superuser:
            return super().get_queryset(request)
        
        data = self.get_model_objects(request)
        return data
    
    def get_model_objects(self, request, action=None, klass=None):
        opts = self.opts
        action =[action] if action else ['view', 'edit', 'delete']
        klass = klass if klass else opts.model
        model_name = klass._meta.model_name
        return get_objects_for_user(user=request.user, perms=[f'{perm}_{model_name}' for perm in action], klass=klass, any_perm=True)
    
    def has_permission(self, request,obj, action):
        opts = self.opts
        code_name = f'{action}_{opts.model_name}'
        if obj:
            return request.user.has_perm(f'{opts.app_label}.{code_name}', obj)
        else:
            return True
        
    def has_add_permission(self, request, obj = None):
        return self.has_permission(request, obj, 'add')
    
    
    def has_view_permission(self, request, obj = None):
        return self.has_permission(request, obj, 'view')    
    
    def has_change_permission(self, request, obj = None):
        return self.has_permission(request, obj, 'change')
    
    def has_delete_permission(self, request, obj = None):
        return self.has_permission(request, obj, 'delete')

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