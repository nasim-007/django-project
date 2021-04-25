from django.shortcuts import render

from .models import Profile

# Create your views here.

def homepage(request):

    profile = Profile.objects.all()

    context = {
       'profile': profile
    }

    return render(request, 'index.html', context)