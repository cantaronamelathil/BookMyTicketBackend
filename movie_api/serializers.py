from rest_framework import serializers
from .models import Movie,Images,Cast



class MovieHomeApiSerializer(serializers.ModelSerializer):
    '''
    Home page api
    '''
    class Meta:
        model = Movie
        fields = ['image','name','rating']
        
    image = serializers.SerializerMethodField()
    
    def get_image(self,obj):
        if image_instance := Images.objects.filter(movie=obj).first():
            return image_instance.image.url
        return None


class ImageAllFieldsSerializer(serializers.ModelSerializer):
    '''
    images model all data fetch based on movie object
    '''
    class Meta:
        model = Images
        fields = ['image']
    

class CastAllFieldsSerializer(serializers.ModelSerializer):
    '''
    cast model all data fetch based on movie object
    '''
    class Meta:
        model = Cast
        fields = ['image','name']


class MovieDetailsFetchSerializer(serializers.ModelSerializer):
    '''
    All detail view api,
    fetch Cast model data,
    fetch Images model data,
    '''
    class Meta:
        model = Movie
        fields = ['name','rating','about','genere','language','release_date','duration','images','cast']
    
    images = serializers.SerializerMethodField()
    cast = serializers.SerializerMethodField()
    
    def get_images(self,obj):
        if instance:=Images.objects.filter(movie=obj):
            return ImageAllFieldsSerializer(instance=instance,many=True).data
        return None
    
    def get_cast(self,obj):
        if instance:=Cast.objects.filter(movie=obj):
            return CastAllFieldsSerializer(instance=instance,many=True).data
        return None
        