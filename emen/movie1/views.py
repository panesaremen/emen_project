import os

import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django .shortcuts import render,redirect
from django.urls import reverse
from emen import settings

from .models import Movie, UploadForm
from .upload_video import upload_to_youtube

url = "https://www.googleapis.com/youtube/v3/activities?part=snippet,contentDetails&channelId=UCeAfYQa-0HhbYC0b9xwjDSw&key=AIzaSyDlRaBh4mk8bzvfg4uQV-unhvSIiKHGjdY"

@login_required
def index(request):
    all_movies = Movie.objects.all()

    context = {

        'all_movies': all_movies,

    }
    return render(request, 'movie1/index.html', context)


@login_required
def detail(request,movie_id):
    return HttpResponse("<h1> welcome to movies number:" + str(movie_id) + "</h1>")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'movie1/register.html', {'form': form})

@login_required
def youtube_search(request, **kwargs):
    all_data = requests.get(url).json()
    form = UploadForm()  # A empty, unbound form
    return render(request, 'movie1/youtubepage.html', {'all_data': all_data, 'form': form})


def upload_handler(request):
    # Handle file upload
    if request.method == 'POST':
        uploadForm = UploadForm(request.POST, request.FILES)
        if uploadForm.is_valid():
            uploadForm.save()
            upload_to_youtube(os.path.join(settings.MEDIA_ROOT, 'mydocs/') + request.FILES['file'].name)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('youtube_search'))


