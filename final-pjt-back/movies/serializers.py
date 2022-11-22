from rest_framework import serializers
from .models import Movie, Genre, Rate, Similar
from articles.models import Card

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('poster_path', 'title')

class MovieGenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    card = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class MovieSimilarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Similar
        fields = '__all__'

class MoviewithSimilarListSerializer(serializers.ModelSerializer):

    class GenreListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = '__all__'
    
    similar_set = MovieSimilarListSerializer(many=True, read_only=True)
    genres = GenreListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class MovieRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'
        read_only_fields = ('user', 'movie')


# class ArticleSerializer(serializers.ModelSerializer):
#     comment_set = CommentSerializer(many=True, read_only=True)
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
#     username = serializers.CharField(source='user.username', read_only=True)

#     class Meta:
#         model = Article
#         fields = '__all__'
#         read_only_fields = ('user', )