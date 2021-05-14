from django.shortcuts import render, get_object_or_404
from .models import Property

def property(request):
    property = Property.objects
    return render(request, 'property/propertyview.html', {'property':property})
