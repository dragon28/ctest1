from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import DemoTable

def index(request):
    return HttpResponse("Demo Table Index Page. This is a test.")

def all(request):
    demotabledata = DemoTable.objects.all()
    context = { 'demotabledata' : demotabledata }
    return render(request, "demotable/all.html", context)

def filterid(request, id):
    demotabledata = DemoTable.objects.filter(id=id)
    context = { 'demotabledata' : demotabledata }
    return render(request, "demotable/all.html", context)
