from django.shortcuts import render,redirect
from .forms import Albumform
from . import models
from . import forms

# Create your views here.

def add_Album(request):
    if request.method == 'POST':
        album = Albumform(request.POST)
        if album.is_valid():
            album.save()
           
    else:
        album = Albumform()
    return render(request,'album_form.html',{'form':album})


def edit(request, id):
    post = models.Album.objects.get(pk=id) 
    post_form = forms.Albumform(instance=post)
    if request.method == 'POST': 
        post_form = forms.Albumform(request.POST, instance=post) 
        if post_form.is_valid():
            post_form.save()
        return redirect('homepage')
    
    return render(request, 'album_form.html', {'form' : post_form})

def delete(request, id):
    post = models.Album.objects.get(pk=id) 
    post.delete()
    return redirect('homepage')
    