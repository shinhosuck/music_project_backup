from music.forms import CreateAlbumForm, CreateSongForm, AlbumUpdateForm, SongUpdateForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from music.models import Album, Song, Category
from django.contrib.auth.models import User
from django.contrib import messages
from mutagen.mp3 import MP3
import math


def landing_page(request):
    return render(request, "music/landing_page.html", {})

def home(request):
    album_set = []
    albums = Album.objects.all()
    genres = Category.objects.all()
    for genre in genres:
        album_set += genre.album_set.all()[0:1]
    context = {
        'albums': albums,
        'album_set': album_set
    }
    return render(request, 'music/home.html', context)

@login_required
def detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'music/detail.html', {'album': album})


@login_required
def my_albums(request, pk):
    genres = []
    genre_count = {}
    total_genres = []
    max_num = 0
    user = User.objects.get(pk=pk)
    albums = user.album_set.all()
    for album in albums:
        if album.genre.name not in genres:
            genres.append(album.genre.name)
        total_genres.append(album.genre.name)
    for g in total_genres:
        genre_count[g] = total_genres.count(g)
    if not total_genres:
        max_num = 0
    else:
        max_num = max(genre_count.values())
    context = {
        'genres': genres,
        "max_num": max_num,
    }
    return render(request, 'music/my_albums.html', context)


@login_required
def create_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, f'User {request.user.username}, you have successfully created album "{form.instance}".')
            return redirect("music:home")
    else:
        form = CreateAlbumForm()
    return render(request, 'music/create_album.html', {'form': form})

@login_required
def album_update(request, pk):
    user = request.user
    album = Album.objects.get(pk=pk)
    albums = user.album_set.all()
    if album in albums:
        if request.method == "POST":
            album_update_form = AlbumUpdateForm(request.POST, request.FILES, instance=album)
            if album_update_form.is_valid():
                album_update_form.save()
                messages.success(request, f"Album \"{album}\" has been updated")
            return redirect("music:my_albums", pk=request.user.pk)
        else:
            album_update_form = AlbumUpdateForm(instance=album)
        context = {
            "album_update_form": album_update_form,
        }
        return render(request, "music/album_update.html", context)
    else:
        messages.success(request, f"Request denied. You are not authorized to update this album.")
    return redirect("music:detail", pk=pk)


@login_required
def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    user = request.user
    my_albums = user.album_set.all()
    if album in my_albums:
        album.delete()
        messages.success(request, f"Album \"{album}\" has been deleted")
        return redirect("music:my_albums", pk=user.id)
    else:
        context = {
            "message": "Sorry, your request has been denied."
        }
    return render(request, "music/404.html", context)


def album_warning_message(request, pk):
    album = Album.objects.get(pk=pk)
    user = request.user
    context = {
        "message": f"User {user.username}, are you sure you want to delete album \"{album}\"?",
        "album": album,
        "user": user
    }
    return render(request, "music/album_warning_message.html", context)


@login_required
def create_song(request, pk):
    user = request.user                 # request user
    albums = user.album_set.all()       # get users albums
    album = Album.objects.get(pk=pk)    # get the current album
    if album in albums:
        if request.method == 'POST':
            song_form = CreateSongForm(request.POST, request.FILES)
            song_form.instance.album = album # set it to the current album
            if song_form.is_valid():
                song_form.save()
                messages.success(request, f'User {request.user.username}, your song has been successfully added.')
            return redirect('music:detail', pk=pk)
        else:
            song_form = CreateSongForm()
        context = {
            "song_form": song_form
        }
        return render(request, 'music/create_song.html', context)
    else:
        messages.success(request, f"Request denied. You are not authorized to add song to this album.")
    return redirect("music:detail", pk=pk)


@login_required
def song_update(request, album_pk, song_pk):
    user = request.user
    album = Album.objects.get(pk=album_pk)
    albums = user.album_set.all()
    if album in albums:
        song = Song.objects.get(pk=song_pk)
        if request.method == "POST":
            song_update_form = SongUpdateForm(request.POST, instance=song)
            if song_update_form.is_valid():
                song_update_form.save()
                messages.success(request, f"Song \"{song}\" has been updated")
            return redirect("music:detail", pk=album_pk)
        else:
            song_update_form = SongUpdateForm(instance=song)
        context = {
            "song_update_form": song_update_form,
            "album_pk": album_pk,
            "song_pk": song_pk
        }
        return render(request, "music/song_update.html", context)
    else:
        song = Song.objects.get(pk=song_pk)
        messages.warning(request, "Request denied. You are not authorized to update this song.")
    return redirect("music:detail", pk=album_pk)


@login_required
def delete_song(request, album_pk, song_pk):
    user = request.user
    album = Album.objects.get(pk=album_pk)
    albums = user.album_set.all()
    if album in albums:
        songs = album.song_set.all()
        song = Song.objects.get(pk=song_pk)
        if song in songs:
            song.delete()
            messages.success(request, f"Song \"{song}\" has been deleted")
            return redirect("music:detail", pk=album_pk)
    else:
        context = {
            "message": "Sorry, your request has been denied."
        }
        return render(request, "music/404.html", context)

def song_warning_message(request, album_pk, song_pk):
    user = request.user
    album = Album.objects.get(pk=album_pk)
    albums = user.album_set.all()
    if album in albums:
        songs = album.song_set.all()
        song = Song.objects.get(pk=song_pk)
        user = request.user
        if song in songs:
            context = {
                "message": f"User {user.username}, are you sure you want to delete song \"{song}\"?",
                "album": album,
                "user": user,
                "song": song
            }
            return render(request, "music/song_warning_message.html", context)
    else:
        context = {
            "message": "Sorry, your request has been denied."
        }
        return render(request, "music/404.html", context)


def play_album(request, pk):
    song_length = []
    album = Album.objects.get(pk=pk)
    songs = album.song_set.all()
    for song in songs:
        audio = MP3(song.file_song)
        audio_length = audio.info.length
        minute = str(math.trunc((audio_length % 3600) / 60))
        second = str(math.trunc(audio_length % 60))
        if len(second) == 1:
            song_length.append(f"{minute}:0{second}")
        elif len(second) < 1:
            song_length.append(f"{minute}:00{second}")
        elif len(minute) < 1:
            song_length.append(f"0{minute}:{second}")
        else:
            song_length.append(f"{minute}:{second}")
    context = {
        "album": album,
        "song_length": song_length
    }
    return render(request, "music/play_album.html", context)


@login_required
def album_likes(request, pk):
    user = request.user
    album = Album.objects.get(pk=pk)
    users = album.likes.all()
    if user not in users:
        album.likes.add(user)
    else:
        pass
    print(user)
    print(users)
    return redirect("music:play_album" , pk=pk)






