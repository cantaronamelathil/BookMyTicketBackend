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
    release_data = models.DateTimeField()
    duration = models.FloatField()



class Images(models.Model):
    movie = models.ForeignKey("movie_api.Movie", on_delete=models.CASCADE)
    image = models.ImageField()
    

class Cast(models.Model):
    movie = models.ForeignKey("movie_api.Movie", on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=50)
    
