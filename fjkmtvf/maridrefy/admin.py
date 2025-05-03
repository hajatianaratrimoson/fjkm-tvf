from django.contrib import admin
from maridrefy.models import Sondage
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class SondageResource(resources.ModelResource):
    class Meta:
        model = Sondage
        fields = ['anonymous']

@admin.register(Sondage)
class SondageAdmin(ImportExportModelAdmin):
    resource_classes = [SondageResource]
    # inlines = [BatisaAdminInline,KatekomenaAdminInline, MpandrayAdminInline, MpikambanaAdminInline ]
    readonly_fields = ['anonymous']
    list_display = ['anonymous']
    #list_filter = ['anonymous', 'sigara']
    
    #Activate search field on model
    search_fields = ['anonymous']
