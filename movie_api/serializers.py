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
    
    images = ImageAllFieldsSerializer(many=True)
    cast = CastAllFieldsSerializer(many=True)
    
