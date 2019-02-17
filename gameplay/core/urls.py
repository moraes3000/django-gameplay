from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import AdminTemplateView

urlpatterns = [

    path('admin-admin/', login_required(AdminTemplateView.as_view()), name='AdminTemplateView'),
    # path('upload',upload, name='ckeditor_upload'),
    # path('browse',browse, name='ckeditor_browse'),
    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
   
]