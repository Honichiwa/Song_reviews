from django.urls import path
from . import views

urlpatterns = [
    path('',views.SongReviewList.as_view()),
    path('<int:pk>/', views.SongReviewDetail.as_view()),
    path('<int:pk>/like/', views.SongReviewLikeCreateDestroy.as_view()),
    path('<int:songreview_pk>/comments/', views.SongReviewCommentList.as_view()),
    path('comment/<int:pk>/', views.SongReviewCommentDetail.as_view()),
    path('songs/', views.SongList.as_view()),
    
]
