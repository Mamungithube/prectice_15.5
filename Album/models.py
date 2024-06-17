from django.db import models
from musician.models import musician

# Create your models here.
class Album(models.Model):
    Album_Name=models.CharField(max_length=50)
    musician_model= models.ForeignKey(musician, on_delete=models.CASCADE, default=None)
    Album_release_date=models.DateField()
    Rating = models.IntegerField()

    def __str__(self):
        return self.Album_Name