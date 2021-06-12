from django.urls import path
from .views import PostsView, PostDetailView, PostAddView, CommentAddView

urlpatterns = [
    path('', PostsView.as_view(), name="post_list"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('add_post', PostAddView.as_view(), name = "post_add"),
    path('post/<int:pk>/comment', CommentAddView.as_view(), name = "comment_add"),
]