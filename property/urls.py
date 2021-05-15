from . import views
from django.urls import path

urlpatterns = [
    path('<int:property_id>', views.property, name='propertyview'),
]
