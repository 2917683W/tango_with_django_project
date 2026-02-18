from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def index(request):
#    return HttpResponse("Rango says hello world")

#def index(request):
#    return render(request, 'rango/index.html')


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)