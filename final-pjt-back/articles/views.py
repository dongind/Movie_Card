
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import CardListSerializer, CardSerializer, CommentSerializer, RateMovieCardSerializer, CommentListSerializer
from .models import Card, Comment
from movies.models import Movie



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def card_list(request):
    if request.method == 'GET':
        cards = get_list_or_404(Card)
        cardss = get_object_or_404(Card, pk=4)
        # cards[0].movie.rate_set에서 순회
        print(cardss.movie)
        print(cards[3].movie)
        print(request.user.pk)
        serializer = CardListSerializer(cards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # print(request.user.pk)
        # print(request.data['movie'])
        can_write = True
        movie = get_object_or_404(Movie, pk=request.data['movie'])
        # print(movie)
        card_list = get_list_or_404(Card)
        for card in card_list:
            if request.user.pk == card.user.pk:
                if card.movie.pk == int(request.data['movie']):
                    # print(card.movie)
                    if card.is_watched:
                        can_write = False
                    # print(card.is_watched)
        if can_write:
            serializer = CardSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):

                movie_pk = int(request.data['movie'])
                movie = get_object_or_404(Movie, pk=movie_pk)
                serializer.save(user=request.user, movie=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def card_mylist(request):
    if request.method == 'GET':
        cards = Card.objects.filter(user=request.user.pk)
        serializer = CardListSerializer(cards, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def card_detail(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)

    if request.method == 'GET':
        serializer = RateMovieCardSerializer(card)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def like_card(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    user = request.user
    if card.like_users.filter(pk=user.pk).exists():
        card.like_users.remove(user)
        serializer = CardSerializer(card)
        return Response(serializer.data)
    else:
        card.like_users.add(user)
        serializer = CardSerializer(card)
        return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, card_pk):
    card = get_object_or_404(Card, pk=card_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(card=card)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
