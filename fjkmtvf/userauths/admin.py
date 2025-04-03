from django.contrib import admin

# Register your models here.
from userauths.models import User

# Register your models here.
"""Every mixte changing of Admin Dashboard displaying
"""

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']
    search_fields = ['username', 'email']
    
admin.site.register(User, UserAdmin)