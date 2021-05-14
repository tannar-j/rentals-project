
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('property/', include('property.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('createaccount/', include('createaccount.urls')),
    path('signin/', include('signin.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
