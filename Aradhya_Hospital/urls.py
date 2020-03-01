from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient_view/',include('patient_data.urls')),
    path('authentication/',include('Authentication.urls')),
    path('gallery_view/',include('AradhyaGallery.urls')),
    path('',views.home,name='home'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)