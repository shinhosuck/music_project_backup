from django.urls import path
from music.views import (
                        landing_page,
						home,
						detail,
						my_albums,
						create_album,
						create_song,
						album_update,
						delete_song,
						song_update,
						delete_album,
						play_album,
						album_warning_message,
						song_warning_message,
						album_likes
					)

app_name = 'music'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('home/', home, name='home'),
    path('album/<int:pk>/detail/', detail, name='detail'),
    path('user/<int:pk>/albums/', my_albums, name='my_albums'),
    path('new/album/', create_album, name='create_album'),
    path('album/<int:pk>/delete', delete_album, name='delete_album'),
    path('album/<int:pk>/add_song/', create_song, name='create_song'),
    path('album/<int:pk>/update/', album_update, name='album_update'),
    path('album/<int:album_pk>/song/<int:song_pk>/update/', song_update, name='song_update'),
	path('album/<int:album_pk>/song/<int:song_pk>/delete/', delete_song, name='song_delete'),
	path('page/not/found/', delete_album, name='page_404'),
	path('album/<int:pk>/play/', play_album, name='play_album'),
	path('album/<int:pk>/delete/message/', album_warning_message, name="album_warning_message"),
	path('album/<int:album_pk>/song/<int:song_pk>/delete/message/', song_warning_message, name="song_warning_message"),
	path('album/<int:pk>/likes', album_likes, name="album_likes")
]
