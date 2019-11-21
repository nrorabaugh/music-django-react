from rest_framework import serializers

from .models import Artist, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'album', 'photo_url')

class ArtistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    class Meta: 
        model = Artist
        fields = ('id', 'name', 'nationality', 'photo_url', 'songs')