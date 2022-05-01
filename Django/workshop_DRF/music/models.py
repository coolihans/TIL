from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)


class Music(models.Model):
    # 반대 방향이 낫지 않나
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    artist = models.ManyToManyField()
    title = models.CharField(max_length=200)