from django.shortcuts import render, get_object_or_404
from .models import Movie

def view_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, '../../../PycharmProjects/vascoflix/templates/view_movie.html', {'movie': movie})


def list_videos(request):
    videos = Movie.objects.all()
    return render(request, '../../../PycharmProjects/vascoflix/templates/list_videos.html', {'videos': videos})