from django.shortcuts import render

from .models import Profile

# Create your views here.

def homepage(request):

    profile = Profile.objects.all()

    context = {
       'profile': profile
    }

    return render(request, 'myapp/index.html', context)

def blueberry(request):

    
    context = {
       
    }

    return render(request, 'blueberry.html', context)