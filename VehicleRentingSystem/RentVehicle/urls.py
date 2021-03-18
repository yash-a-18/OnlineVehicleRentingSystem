from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name="Home"),
    path('SendRequest_toOwner/',views.SendRequest_toOwner,name="SendRequest_to_Owner"),
    path('/Owner',include("Owner.urls")),
    path('/Manager',include("Manager.urls"))
]