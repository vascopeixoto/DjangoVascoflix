from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Movie, VideoHistory


@login_required
def view_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.user.is_authenticated:
        VideoHistory.objects.create(user=request.user, video=movie)

    return render(request, '../../../PycharmProjects/vascoflix/templates/view_movie.html', {'movie': movie})


@login_required
def list_videos(request):
    videos = Movie.objects.filter(active=True)
    return render(request, '../../../PycharmProjects/vascoflix/templates/list_videos.html', {'videos': videos})


def custom_login(request):
    if request.user.is_authenticated:
        print("Utilizador já autenticado:", request.user)
        return redirect('list_videos')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_videos')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required
def video_history(request):
    history = VideoHistory.objects.filter(user=request.user).order_by('-date_viewed')
    return render(request, 'history.html', {'history': history})
