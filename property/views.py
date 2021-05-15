from django.shortcuts import render, get_object_or_404
from .models import Property

def property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    return render(request, 'property/propertyview.html', {'property':property})
