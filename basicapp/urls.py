from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview),
    path('posts/', views.PostView.as_view()),
    #path('comment/', views.CommentView.as_view()),
    #path('posts/<str:pk>/', views.PostDetailView.as_view()),
    path('posts/comments/<str:pk>/', views.CommentAddToPost.as_view()),
    #path('posts/comments/<str:pk>/', views.add_comment),
    path('posts/detail/<str:pk>/', views.PostDetailView.as_view()),
    path('users/', views.UserView.as_view()),
    path('users/<str:pk>/', views.UpdateUserView.as_view()),
]