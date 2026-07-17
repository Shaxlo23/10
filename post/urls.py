from django.urls import path
from . import views


urlpatterns = [
    path('post/',views.PostListAPIView.as_view(),name="post-list"),
    path('post/create/',views.PostCreateAPIView.as_view(),name="post-create"),
    path('post/<int:pk>/',views.PostRetrieveAPIView.as_view(),name="post-detail"),
    path('post/update/<int:pk>/',views.PostUpdateAPIView.as_view(),name="post-update"),
    path('post/delete/<int:pk>/',views.PostDestroyAPIView.as_view(),name="post-update"),
    path('post/detail-update/<int:pk>/',views.PostRetrieveUpdateAPIView.as_view(),name="post-update"),
    path('post/detail-delete/<int:pk>',views.PostRetrieveDestroyAPIView.as_view(),name="post-detail-delete"),
    path('post/<int:pk>/manage/',views.PostRetrieveUpdateDestroyAPIView.as_view(),name="post-manage"),
]