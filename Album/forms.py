from django import forms
from .models import Album

class Albumform(forms.ModelForm):
    class Meta: 
        model = Album
        fields = '__all__'

        widgets = {
            'Rating': forms.Select(choices=[(i,i) for i in range(1,6)]),
            'Album_release_date': forms.NumberInput(attrs={'type':'date'}),
        }