from django.shortcuts import render, get_object_or_404

def createaccount(request):
    return render(request, 'createaccount/createaccount.html')
