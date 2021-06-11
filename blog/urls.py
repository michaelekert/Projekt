from django.urls import path
from .views import PostsView, PostDetailView, PostAddView

urlpatterns = [
    path('', PostsView.as_view(), name="post_list"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('add_post', PostAddView.as_view(), name = "post_add"),
]