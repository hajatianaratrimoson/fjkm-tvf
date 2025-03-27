from django.contrib import admin

# Register your models here.
from userauths.models import User

# Register your models here.
"""Every mixte changing of Admin Dashboard displaying
"""

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']
    
admin.site.register(User, UserAdmin)