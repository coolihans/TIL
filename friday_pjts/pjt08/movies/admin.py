from django.contrib import admin
from .models import Movie, Actor, Review

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'overview', 'release_date', 'poster_path')


admin.site.register(Movie, MoviesAdmin)
admin.site.register(Actor)
admin.site.register(Review)
