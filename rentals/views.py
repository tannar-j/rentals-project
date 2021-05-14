from django.http import HttpResponse
from django.shortcuts import render
from property.models import Property

def home(request):
    properties = Property.objects
    return render(request, 'home.html',{'properties': properties})
