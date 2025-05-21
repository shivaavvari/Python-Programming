from myapp.models import Movie
from rest_framework import serializers 

class MovieSerializer(serializers.ModelSerializer):
    images = serializers.ImageField(max_length = None, use_url=True)
    class Meta:
        model = Movie
        fields =['name','description','ratings','images']

