from music.models import Album, Song
from django import forms


class CreateAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['title', 'artist', 'genre', 'album_cover']

class CreateSongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['title', 'file_type', 'file_song']

class AlbumUpdateForm(forms.ModelForm):
	
    class Meta:
        model = Album 
        fields = ["title", "artist", "genre", "album_cover"]

class SongUpdateForm(forms.ModelForm):
	
    class Meta:
        model = Song
        fields = ["title", 'file_type', 'file_song']