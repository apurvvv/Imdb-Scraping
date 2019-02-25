from django.db import models


# Class for the name and ratings of the movie.
class Movie(models.Model):
    owner = models.ForeignKey('auth.User', related_name='movie', on_delete=models.CASCADE, default=1)
    movie_name = models.CharField(max_length=100)
    movie_star = models.FloatField(max_length=15)
    movie_description = models.TextField(max_length=5000, default="Description")
    movie_pic = models.URLField(max_length=300)

    def __str__(self):
        return "%s %s" % (self.movie_name, self.movie_star)


# Class for cast and character in the movie.
class Role(models.Model):
    cast = models.ForeignKey(Movie, related_name='roles', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)

    def __str__(self):
        return '%s: %s' % (self.name, self.character)
