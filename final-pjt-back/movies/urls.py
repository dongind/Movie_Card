from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/latest/', views.movie_latest),
    path('movies/popular/', views.movie_popular),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/rate/', views.movie_rate),
    path('movies/recommend/user/', views.user_recommend),
    path('movies/genre/<int:genre_pk>/', views.movie_genre),
    # path('articles/<int:article_pk>/comments/', views.comment_create),
    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI (스웨거 페이지)
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
