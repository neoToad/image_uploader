from django.urls import path

from . import views

app_name = 'image_boards'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post, name='post'),
    path('new_post/', views.new_post, name='new_post'),
    path('my_post/', views.my_posts, name='my_posts'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('user_posts/<int:user_id>/', views.user_posts, name='user_posts')
]