from django.db import models

#created three models- Artiste, Song, Lyric

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    date = models.dateField()
    released = models.date()
    likes = models.IntegerField()

    def __str__(self):
        return self.name


class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.cascade, null=True, blank=True)
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.name
