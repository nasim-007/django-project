from django.shortcuts import render

from carousel.models import Carousel

# Create your views here.


def caroseltest(request):

    carousel = Carousel.objects.all()

    context = {

        'carousel': carousel

    }

    return render(request, 'carousel/index.html', context)