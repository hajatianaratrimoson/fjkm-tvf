"""
URL configuration for fjkmtvf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# css & js Synchroniser 15/01/25
from django.conf import settings
from django.conf.urls.static import static
#Library using i18n for local language Universal
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mpandraharaha.urls")),
    
    # path('user/', include("userauths.urls")),
    
    path("ckeditor/", include("ckeditor_uploader.urls")),
    #Url pointing local i8n language select
    path("i18n/", include("django.conf.urls.i18n")),
]
# Another Url pointing local i8n language select
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

"""
- activate when debug is true
- load all css & js & images (static & media)
- 15/01/25
"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)