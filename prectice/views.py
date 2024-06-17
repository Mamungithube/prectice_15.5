from django.shortcuts import render, redirect
from Album.models import Album
# Create your views here.


def home(request):
    data = Album.objects.all()
    return render(request, 'index.html', {'data' : data})
