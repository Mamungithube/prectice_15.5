from django.shortcuts import render
from .forms import Albumform

# Create your views here.

def add_Album(request):
    if request.method == 'POST':
        album = Albumform(request.POST)
        if album.is_valid():
            album.save()
           
    else:
        album = Albumform()
    return render(request,'album_form.html',{'form':album})