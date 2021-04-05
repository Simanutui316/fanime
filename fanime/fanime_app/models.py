from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

#Im thinking instead of saving all the anime info we save the anime id or the anime link
#for example cowboy bebop id is 1 and the link is https://kitsu.io/api/edge/anime/1 
#I think we can work with that
class FavList(models.Model):
    api_link = models.CharField(max_length=100)
    api_id = models.CharField(max_length=10)
    api_name = models.CharField(max_length=100)


class Profile(models.Model):
    name = models.CharField(max_length=100)
    favorite_anime_ever = models.CharField(max_length=100)
    about = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_anime_id = models.IntegerField()
    fav_anime_name = models.CharField(max_length=100)
    fav_list = models.ManyToManyField(FavList)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile')

class Photo(models.Model):
    url = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for profile_id: {self.profile_id} @{self.url}"

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    anime_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Search(models.Model):
    search = models.CharField(max_length=100)

