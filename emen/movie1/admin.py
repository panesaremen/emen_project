from django.contrib import admin
from .models import Movie
from .models import Song
from .models import upload
admin.site.register(Movie)
admin.site.register(Song)
admin.site.register(upload)
