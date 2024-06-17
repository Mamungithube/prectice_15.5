from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def add_musician(request):
    if request.method == 'POST':
        add_musician = forms.musicianForm(request.POST)

        if add_musician.is_valid():
            add_musician.save()
            
    else:
        add_musician = forms.musicianForm()
        print(add_musician)
    return render(request,'musician_form.html',{'form':add_musician})
