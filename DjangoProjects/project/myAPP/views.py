from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    #return HttpResponse('shenyanyu is a good man')
    return render(request, 'myAPP/index.html')