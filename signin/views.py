from django.shortcuts import render, get_object_or_404

def signin(request):
    return render(request, 'signin/signin.html')
