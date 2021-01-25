from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Genres'


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=100)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    album_cover = models.ImageField(default='default_cover.jpg', upload_to='album_covers')
    likes = models.ManyToManyField(User, related_name="album_likes")

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.album_cover.path)
        if img.width > 500 or img.height > 500:
            new_img = (400, 400)
            img.thumbnail(new_img)
            img.save(self.album_cover.path)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_song = models.FileField(upload_to="songs")
    title = models.CharField(max_length=120)
    file_type = models.CharField(max_length=10)
    date_added = models.DateTimeField(default=timezone.now)

    # class Meta:
    #     ordering = ["-date_added"]

    def __str__(self):
        return self.title



