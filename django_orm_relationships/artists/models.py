from django.db import models


GENRE_CHOICES = (
    ("rock", "Rock"),
    ("blues", "Blues"),
)

class Artist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    artistic_name = models.CharField(max_length=255)
    picture_url = models.URLField()
    popularity = models.IntegerField()
    genre = models.CharField(choices=GENRE_CHOICES, max_length=255)

    def __str__(self):
        return self.artistic_name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255, blank=True)
