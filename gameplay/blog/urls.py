from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='PostListView'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),


    #admin
    path('admin-post', views.AdminPostView.as_view(), name='admin-post'),
    path('novo/', views.PostCreateView.as_view(), name='PostCreateView'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete-post'),
    path('admin-post/<int:pk>', views.AdminPostUpdate.as_view(), name='AdminPostUpdate'),


]