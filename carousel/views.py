from django.shortcuts import render

# Create your views here.


def caroseltest(request):

    context = {
       
    }

    return render(request, 'carousel.html', context)