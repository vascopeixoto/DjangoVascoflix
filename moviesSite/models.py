from django.db import models
from django.contrib import admin


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    genre = models.CharField(max_length=150)
    producer = models.CharField(max_length=150)
    image = models.FileField(blank=True)
    video = models.FileField(blank=True)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'producer', 'date', 'video', 'image')


admin.site.register(Movie, MovieAdmin)
