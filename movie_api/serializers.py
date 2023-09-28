from rest_framework import serializers
from .models import Movie,Images,Cast



class MovieHomeApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['image','name','rating']
        
    image = serializers.SerializerMethodField()
    
    def get_image(self,obj):
        image_instance = Images.objects.filter(movie=obj).first()
        if image_instance:
            return image_instance.image.url
        return None
    


class ImageAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['image']
    

class CastAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ['image','name']


class MovieDetailsFetchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['name','rating','about','genere','language','release_date','duration','images','cast']
    
    images = serializers.SerializerMethodField()
    cast = serializers.SerializerMethodField()
    
    def get_images(self,obj):
        instance = Images.objects.filter(movie=obj)
        if instance:
            return ImageAllFieldsSerializer(instance=instance,many=True)
        return None
    
    def get_cast(self,obj):
        instance = Cast.objects.filter(movie=obj)
        if instance:
            return CastAllFieldsSerializer(instance=instance,many=True)
        return None
        