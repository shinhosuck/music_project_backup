from django.contrib import admin
from music.models import Album, Song, Category


admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Category)

