from django.urls import path

from .views import (PostListView, PostDetailView, AboutView, PostCreateView, PostDeleteView, PostUpdateView, \
                    UserPostListView)

urlpatterns = [
    path('', PostListView.as_view(template_name='post_list.html'), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(template_name='user_post_list.html'), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(template_name='post_detail.html'), name="post-detail"),
    path('post/new/', PostCreateView.as_view(template_name='post_form.html'), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name='post_form.html'), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name='post_confirm_delete.html'), name="post-delete"),
    path('about/', AboutView.as_view(template_name='about.html'), name="blog-about"),

]
