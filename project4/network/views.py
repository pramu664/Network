from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



def index(request):
    return render(request, "network/index.html")

