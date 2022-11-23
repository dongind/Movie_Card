from rest_framework import serializers
from .models import Card, Comment
from movies.models import Movie, Rate
from django.db.models import Prefetch

class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'
        read_only_fields = ('user_id',)

class CardListSerializer(serializers.ModelSerializer):

    class MovieTitleSerializer(serializers.ModelSerializer):
        
        rate_set = RateSerializer(many=True, read_only=True)
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path', 'backdrop_path', 'rate_set')


    movie = MovieTitleSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Card
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('card_id',)

class CommentSerializer(serializers.ModelSerializer):

    class CardTitleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Card
            fields = ('movie',)

    card = CardTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class RateMovieCardSerializer(serializers.ModelSerializer):

    class RateMovieSerializer(serializers.ModelSerializer):

        rate_set = RateSerializer(many=True, read_only=True)

        class Meta:
            model = Movie
            fields = ('__all__')

    movie = RateMovieSerializer(read_only=True)

    class Meta:
        model = Card
        fields = '__all__'
        read_only_fields = ('user',)

class CardSerializer(serializers.ModelSerializer):

    class MovieTitleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title', 'poster_path', 'backdrop_path')

    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Card
        fields = '__all__'
        read_only_fields = ('user', 'like_users', 'movie')