from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    genre = models.CharField(max_length=150)
    producer = models.CharField(max_length=150)
    image = models.FileField(blank=True)
    video = models.FileField(blank=True)
    active = models.BooleanField(default=True)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'producer', 'date', 'video', 'image')


admin.site.register(Movie, MovieAdmin)


class VideoHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date_viewed = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_viewed']
