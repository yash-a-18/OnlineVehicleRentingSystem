from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from CustomerHome import views as cust_views


urlpatterns = [
    path('', views.index, name="Owner"),
    path('signin/',cust_views.signin, name="SignIn"),
    path('Logout/',cust_views.Logout, name="Logout"),
    path('Profile/',views.Profile, name="Profile"),
    path('RegisterManager/',views.register_manager, name="RegisterManager"),
    path('ManagerRegistration/',views.ManagerRegistration, name="ManagerRegistration"),
    path('AllManagers/',views.AllManagers, name="AllManagers"),
    path('AllCustomers/',views.AllCustomers, name="AllCustomers")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)