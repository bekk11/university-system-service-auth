from django.urls import path

from apps.blog.api import BlogCreateAPIView, BlogDestroyAPIView, BlogUpdateAPIView, BlogListAPIView, BlogRetrieveAPIView

urlpatterns = [
    path('list/', BlogListAPIView.as_view()),
    path('create/', BlogCreateAPIView.as_view()),

    path('retrieve/<int:pk>/', BlogRetrieveAPIView.as_view()),
    path('update/<int:pk>/', BlogUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', BlogDestroyAPIView.as_view()),

]