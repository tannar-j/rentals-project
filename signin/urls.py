from . import views
from django.urls import path

urlpatterns = [
    path('', views.signin, name='signin')
]
