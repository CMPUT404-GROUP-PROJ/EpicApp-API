from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('author/<str:id>', views.get_author, name='get_author'),
    path('authors/', views.get_authors, name='get_authors'),

    # post paths
    path('authors/<str:author_id>/posts/', views.posts, name='posts endpoint'),
    path('authors/<str:author_id>/posts/<str:post_id>/', views.post, name="post endpoint"),

    # comment paths
    path('authors/<str:author_id>/posts/<str:post_id>/comments', views.comments, name="comment endpoint")
]