from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

import requests
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer, MoviewithSimilarListSerializer, MovieGenreListSerializer, MovieRateSerializer
from .models import Movie, Genre, Rate
from pprint import pprint



# sklearn module
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from numpy import dot
from numpy.linalg import norm

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MoviewithSimilarListSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


def cosine_similar(N, user_genre_vector, user_overview_vector, genre_vectors, overview_vectors):
    result = [0 for _ in range(N)]
    for i in range(N):
        # genre 코사인 유사도 계산
        if norm(user_genre_vector) * norm(genre_vectors[i]):
            genre_similarity = dot(user_genre_vector, genre_vectors[i]) / (norm(user_genre_vector) * norm(genre_vectors[i]))
        # overview 코사인 유사도 계산
        if norm(user_overview_vector) * norm(overview_vectors[i]):
            overview_similarity = dot(user_overview_vector, overview_vectors[i]) / (norm(user_overview_vector) * norm(overview_vectors[i]))
        # total 코사인 유사도 계산
        result[i] = overview_similarity * genre_similarity
    return result


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_recommend(request):

    all_movies = get_list_or_404(Movie)
    all_genres = get_list_or_404(Genre)

    N = len(all_movies)

    rates = request.user.rate_set.all()
    movie_pk = []
    movie_rate = []
    for rate in rates:
        if rate.rate >= 3:
            movie_pk.append(rate.movie.pk)
            movie_rate.append((rate.rate - 2))
    print(movie_rate)

    # # 1. 유저 장르 벡터 생성
    genre_idx = dict()
    for i in range(19):
        genre_idx[all_genres[i].id] = i
    
    user_genre_vector = [0 for _ in range(19)]
    genre_vectors = [[0 for _ in range(19)] for _ in range(N)]

    for i in range(N):
        for genre in all_movies[i].genres.all():
            index = genre_idx[genre.pk]
            genre_vectors[i][index] = 1
    
    for i in range(len(movie_pk)):
        for genre in all_movies[movie_pk[i] - 1].genres.all():
            index = genre_idx[genre.pk]
            user_genre_vector[index] += (1 * movie_rate[i])

    # 2. 유저 overview 벡터 생성
    countVec = CountVectorizer(max_features=10000, stop_words='english')
    overviews = [0 for _ in range(N)]
    for i in range(N):
        overviews[i] = all_movies[i].overview_en
    overview_vectors = countVec.fit_transform(overviews).toarray()

    user_overview_vector = [0 for _ in range(10000)]
    for i in range(len(movie_pk)):
        for j in range(10000):
            user_overview_vector[j] += overview_vectors[movie_pk[i] - 1][j] * movie_rate[i]

    # 3. cosine similarity 계산
    user_similarity = cosine_similar(N, user_genre_vector, user_overview_vector, genre_vectors, overview_vectors)

    # 4. 추천 영화 추출
    recommend_movie_pk = sorted(list(enumerate(user_similarity)), reverse=True, key=lambda x:x[1])[0:10]
    
    recommend_movies = []
    for pk in recommend_movie_pk:
        selected_movie = get_object_or_404(Movie, pk=(pk[0] + 1))
        if selected_movie.vote_count >= 300 and selected_movie.vote_average >= 6:
            recommend_movies.append(selected_movie)
    recommend_serializer = MovieSerializer(recommend_movies, many=True)

    return Response(recommend_serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_genre(request, genre_pk):
    genre_movie = Movie.objects.filter(genres=genre_pk).order_by('-vote_average')[:20]
    serializer = MovieGenreListSerializer(genre_movie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_latest(request):
    paramDict = dict()
    paramDict.setdefault('api_key', '39748706223d0bc28b79151440a205fc')
    requestData = requests.get('https://api.themoviedb.org/3/movie/now_playing', params=paramDict)
    jsonData = requestData.json()

    latest_movies = []
    for movie_data in jsonData['results']:
        movie_id = movie_data["id"]
        latest_movie_set = Movie.objects.filter(movie_id=int(movie_id))
        for latest_movie in latest_movie_set:
            latest_movies.append(latest_movie)
    latest_serializers = MovieSerializer(latest_movies, many=True)
    return Response(latest_serializers.data)


@api_view(['GET'])
def movie_popular(request):
    popular_movies = get_list_or_404(Movie)[0:10]
    popular_serializers = MovieSerializer(popular_movies, many=True)
    return Response(popular_serializers.data)


@api_view(['GET'])
def movie_popularrandom(request):
    popular_random_movies = get_list_or_404(Movie)[0:100]
    popular_random_serializers = MovieSerializer(popular_random_movies, many=True)
    return Response(popular_random_serializers.data)


@api_view(['POST', 'PUT', 'DELETE'])
def movie_rate(request):
    if request.method == 'POST':
        rate_serializer = MovieRateSerializer(data=request.data)
        if rate_serializer.is_valid(raise_exception=True):
            movie_pk = int(request.data['movie_pk'])
            print(movie_pk)
            movie = get_object_or_404(Movie, pk=movie_pk)
            rate_serializer.save(movie=movie, user=request.user)
            # return Response(rate_serializer, status=status.HTTP_201_CREATED)
            return Response()
    if request.method == 'PUT':
        movie_pk = int(request.data['movie_pk'])
        movie = get_object_or_404(Movie, pk=movie_pk)
        rate = Rate.objects.filter(user=request.user, movie=movie)[0]
        
        rate_serializer = MovieRateSerializer(rate, data=request.data)
        if rate_serializer.is_valid(raise_exception=True):
            rate_serializer.save()
            return Response(rate_serializer.data)
    if request.method == 'DELETE':
        movie_pk = int(request.data['movie_pk'])
        movie = get_object_or_404(Movie, pk=movie_pk)
        rate = Rate.objects.filter(user=request.user, movie=movie)[0]
        rate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
