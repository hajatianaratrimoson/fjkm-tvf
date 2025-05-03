import datetime
from django.contrib import admin
from fitantanambola.models import Rafitra, KaontyTvf, KaontyTossaafiko, Laminasa, Diarimbola, JournalCaisse
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
# from import_export.widgets import ForeignKeyWidget
from import_export import resources, fields
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, NumericRangeFilter





class FilterByUserAuth(GuardedModelAdmin):
    # pass
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
        action =[action] if action else ['add','view', 'edit', 'delete']
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
        
    # def has_add_permission(self, request, obj = None):
    #     return self.has_permission(request, obj, 'add')
    
    
    # def has_view_permission(self, request, obj = None):
    #     return self.has_permission(request, obj, 'view')    
    
    # def has_change_permission(self, request, obj = None):
    #     return self.has_permission(request, obj, 'change')
    
    # def has_delete_permission(self, request, obj = None):
    #     return self.has_permission(request, obj, 'delete')
    

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


class KaontyTvfResource(resources.ModelResource):
    class Meta:
        model = KaontyTvf
        # fields = ['isa', 'anarana', 'rafitra__axe']

@admin.register(KaontyTvf)
class KaontyTvfAdmin(ImportExportModelAdmin):
    resource_classes = [KaontyTvfResource]
    
    list_display = ['isa', 'anarana', 'rafitra']
    list_filter = ['isa', 'anarana', 'rafitra']
    
    #Activate search field on model
    search_fields = ['isa', 'anarana', 'rafitra']


class KaontyTossaafikoResource(resources.ModelResource):
    class Meta:
        model = KaontyTossaafiko
        # fields = ['isa', 'anarana', 'rafitra__axe']

@admin.register(KaontyTossaafiko)
class KaontyTossaafikoAdmin(ImportExportModelAdmin):
    resource_classes = [KaontyTossaafikoResource]
    exclude = ['user', 'tossaafiko']
    list_display = ['tossaafiko', 'kaontytvf','isa', 'anarana']
    list_filter = ['tossaafiko', 'kaontytvf', 'isa', 'anarana']
    
    #Activate search field on model
    search_fields = ['tossaafiko', 'kaontytvf',  'isa', 'anarana']

    def get_queryset(self, request):
        qs = super(KaontyTossaafikoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
class LaminasaResource(resources.ModelResource):
    class Meta:
        model = Laminasa
        # fields = ['tossaafiko__anarana', 'daty', 'asa', 'toerana', 'fanamarihana']

@admin.register(Laminasa)
class LaminasaAdmin(FilterByUserAuth, ImportExportModelAdmin):
    # resource_classes = [LaminasaResource]
    exclude = ['user', 'taona', 'tossaafiko']
    list_display = ['taona','tossaafiko','diarimbola', 'daty', 'asa', 'toerana', 'fanamarihana', 'tombana']
    list_filter = ['taona', 'diarimbola','tossaafiko', 'asa',('daty', DateRangeFilter)]
 
    
    # def get_rangefilter_daty_default(self, request):
    #     return (datetime.date.today, datetime.date.today)
    # def get_rangefilter_daty_title(self, request, field_path):
    #     return 'Daty1 daty2'
    #Activate search field on model
    search_fields = ['taona','tossaafiko','diarimbola', 'daty', 'asa', 'toerana', 'fanamarihana', 'tombana']
    def get_queryset(self, request):
        qs = super(LaminasaAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    

class DiarimbolaResource(resources.ModelResource):
    class Meta:
        model = Diarimbola
        # fields = [ 'kaonty', 'vola', 'fanamarihana']

@admin.register(Diarimbola)
class DiarimbolaAdmin(FilterByUserAuth, ImportExportModelAdmin):
    resource_classes = [DiarimbolaResource]
    exclude = ['user', 'taona', 'tossaafiko']
    list_display = ['taona','tossaafiko','kaonty','vola_holaniana','vola_lany','vola_ambiny','ecart','fanamarihana']
    list_filter = ['taona','tossaafiko','kaonty','vola_holaniana','vola_lany','vola_ambiny','ecart','fanamarihana']
    
    #Activate search field on model
    search_fields = ['taona','tossaafiko','kaonty','vola_holaniana','vola_lany','vola_ambiny','ecart','fanamarihana']

    def get_queryset(self, request):
        qs = super(DiarimbolaAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
class JournalCaisseResource(resources.ModelResource):
    class Meta:
        model = JournalCaisse
        # fields = ['tossaafiko__anarana', 'daty', 'asa', 'toerana', 'fanamarihana']

@admin.register(JournalCaisse)
class JournalCaisseAdmin(FilterByUserAuth, ImportExportModelAdmin):
    resource_classes = [JournalCaisseResource]
    exclude = ['user', 'taona', 'tossaafiko']
    list_display = ['daty','taona','tossaafiko','diarimbola', 'miditra', 'mivoaka', 'ded','pj_ded', 'edr', 'pj_edr','solde','fanamarihana']
    list_filter = ['taona','tossaafiko','diarimbola', 'ded', 'edr',('daty', DateRangeFilter)]
    
    #Activate search field on model
    search_fields = ['daty','tossaafiko','diarimbola', 'daty', 'miditra', 'mivoaka', 'ded','pj_ded', 'edr', 'pj_edr','solde','fanamarihana']

    # def get_queryset(self, request):
    #     qs = super(JournalCaisseAdmin, self).get_queryset(request)
    #     return qs.filter(user=request.user)
    
    def get_queryset(self, request):
        qs = super(JournalCaisseAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    # def save_form(self, request, form, change):
    #     obj = super().save_form(request, form, change)
    #     if not change:
    #         obj.user = request.user
    #     return obj

    # def save_model(self, request, obj, form, change):
    #     print("save enter here")
    #     obj.user = request.user  # Attach the current user
    #     super().save_model(request, obj, form, change)  # Save the object"

# class DedResource(resources.ModelResource):
#     class Meta:
#         model = Ded
#         # fields = ['num_ded', 'daty_ded', 'tossaafiko', 'laminasa','diarimbola', 'fandaniana', 'sata']

# @admin.register(Ded)
# class DedAdmin(FilterByUserAuth, ImportExportModelAdmin):
#     resource_classes = [DedResource]
    
#     list_display = [ 'mpitantsorabola','num_ded', 'daty_ded', 'tossaafiko', 'laminasa','diarimbola', 'fandaniana', 'sata']
#     list_filter = [ 'mpitantsorabola', 'num_ded', 'tossaafiko', 'laminasa','diarimbola', 'fandaniana', 'sata' ]
    
#     #Activate search field on model
#     search_fields = ['mpitantsorabola', 'num_ded', 'daty_ded', 'tossaafiko', 'laminasa','diarimbola', 'fandaniana', 'sata' ]
    

# class FanamarinanaDedResource(resources.ModelResource):
#     class Meta:
#         model = Fanamarinana_ded
#         # fields = ['isa', 'anarana', 'rafitra__axe']

# @admin.register(Fanamarinana_ded)
# class KaontyAdmin(ImportExportModelAdmin):
#     resource_classes = [FanamarinanaDedResource]
    
#     list_display = ['tossaafiko','ded', 'mpanamarina_birao_ssa', 'mpanamarina_toby', 'mpanamarina_birao_tvf']
#     list_filter = ['tossaafiko', 'ded', 'mpanamarina_birao_ssa', 'mpanamarina_toby', 'mpanamarina_birao_tvf']
    
#     #Activate search field on model
#     search_fields = ['tossaafiko', 'ded', 'mpanamarina_birao_ssa', 'mpanamarina_toby', 'mpanamarina_birao_tvf']
