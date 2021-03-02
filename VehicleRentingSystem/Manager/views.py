from django.shortcuts import render, redirect
from django.http import HttpResponse
from Owner.models import Owner
from Manager.models import Manager
from CustomerHome.models import Customer

# Create your views here.
def index(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    index=[1,2,3,4,5,6]
    Message="Welcome Aboard!!"
    return render(request,'Manager_index.html',{'p':index,'Message':Message,'manager':manager})