from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    overview = models.TextField()
    overview_en = models.TextField()
    poster_path = models.CharField(max_length=200)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    backdrop_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)


class Rate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField()


class Similar(models.Model):
    similar1_idx = models.IntegerField()
    similar1_title = models.CharField(max_length=100)
    similar1_poster_path = models.CharField(max_length=200)
    similar2_idx = models.IntegerField()
    similar2_title = models.CharField(max_length=100)
    similar2_poster_path = models.CharField(max_length=200)
    similar3_idx = models.IntegerField()
    similar3_title = models.CharField(max_length=100)
    similar3_poster_path = models.CharField(max_length=200)
    similar4_idx = models.IntegerField()
    similar4_title = models.CharField(max_length=100)
    similar4_poster_path = models.CharField(max_length=200)
    similar5_idx = models.IntegerField()
    similar5_title = models.CharField(max_length=100)
    similar5_poster_path = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # title = models.CharField(max_length=100)
    # poster_path = models.CharField(max_length=200)