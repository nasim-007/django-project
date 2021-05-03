from django.shortcuts import render

# Create your views here.
from .models import Album

# Create your views here.

def album(request):

    albums = Album.objects.all()

    context = {
       'albums': albums
    }

    return render(request, 'album/index.html', context)

def blueberry(request):


    context = {
      
    }

    return render(request, 'album/blueberry.html', context)