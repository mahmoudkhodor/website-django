from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
# Create your views here.


def homepage(request):
    return HttpResponse(request=request,
                        template_name="main/home.html",
                        context={"tutorials": Tutorial.object.all})
