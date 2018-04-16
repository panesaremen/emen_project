from django.db import models
from django.forms import ModelForm
from django.urls import reverse


class Movie(models.Model):
    actor = models.CharField(max_length=30)
    actor_movie = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    movie_logo = models.CharField(max_length=100)

    def __str__(self):
        return self.actor + '---' + self.actor_movie + '---' + self.genre + '---' + self.movie_logo


class Song(models.Model):
    actor = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    song_name= models.CharField(max_length=100)

    def __str__(self):
        return self.song_name


class upload(models.Model):
    title = models.CharField(max_length=200)
    body= models.TextField(max_length=200)
    file = models.FileField('videofile', upload_to='mydocs/')

    def __unicode__(self):
        return unicode(self.file)


class UploadForm(ModelForm):
    class Meta:
        model = upload
        fields = ['file']




