from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from CustomerHome import views as cust_views

urlpatterns = [
    path('', views.index, name="Manager"),
    path('signin/',cust_views.signin, name="SignIn"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)