from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    index=[1,2,3,4,5,6]
    print("here")
    return render(request,'Owner_index.html',{'p':index})