from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [

    # cards
    path('cards/', views.card_list),
    path('cards/my/', views.card_mylist),
    path('cards/<int:card_pk>/', views.card_detail),
    path('<int:card_pk>/like/', views.like_card),

    # comments
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('cards/<int:card_pk>/comments/', views.comment_create),
    
    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI (스웨거 페이지)
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
