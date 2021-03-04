from django.urls import path
from . import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('UploadVehicle/', views.upload_vehicle,name="UploadVehicle"),
    path('Owner/',include("Owner.urls")),
    path('Manager/',include("Manager.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)