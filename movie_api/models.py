from django.db import models

# Create your models here.



class Movie(models.Model):
    
    LANGUAGE_CHOICES = [
        ('malayalam',"Malayalam"),
        ('english','English'),
        ('hindi','Hindi'),
        ('tamil',"Tamil"),
        
    ]
    
    name = models.CharField(max_length=100,db_index=True)
    rating = models.IntegerField()
    about = models.TextField()
    genere = models.CharField(max_length=50)
    language = models.CharField(max_length=10,choices=LANGUAGE_CHOICES)
    release_date = models.DateField(auto_now_add=True)
    duration = models.FloatField()

    def __str__(self) -> str:
        return self.name


class Images(models.Model):
    movie = models.ForeignKey("movie_api.Movie", on_delete=models.CASCADE,related_name='image')
    image = models.ImageField(upload_to='movie_images/')
    
    def __str__(self) -> str:
        return f"{self.movie.name} Images"
class Cast(models.Model):
    movie = models.ForeignKey("movie_api.Movie", on_delete=models.CASCADE,related_name='cast')
    image = models.ImageField(upload_to='movie_cast_images/')
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.movie
