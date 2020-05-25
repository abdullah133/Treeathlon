from django.urls import path
from . import views
from django.conf.urls import url
from .views import PostListView, PostDetailView

app_name = 'post_app'

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_page'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail_page'),

]
