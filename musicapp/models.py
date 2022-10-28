from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

class Song(models.Model):
    # Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField() 
    artiste_id = models.AutoField(primary_key=True)
    

class Lyric(models.Model):
    # Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    song_id = models.AutoField(primary_key=True)

