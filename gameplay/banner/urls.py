from django.urls import path
from . import views

urlpatterns = [
    path('novo', views.BannerCreateView.as_view(), name='BannerCreateView'),
    path('lista', views.BannerListView.as_view(), name='BannerListView'),
    path('delete/<int:pk>', views.BannerDeleteView.as_view(), name='BannerDeleteView'),
    path('update/<int:pk>', views.BannerUpdate.as_view(), name='BannerUpdate'),


    path('lista-foto', views.FotoBannerListView.as_view(), name='FotoBannerListView'),
    path('novo-foto', views.FotoCreateView.as_view(), name='FotoCreateView'),
    path('delete-foto/<int:pk>', views.FotorDelete.as_view(), name='FotorDelete'),
    path('update-foto/<int:pk>', views.FotoUpdate.as_view(), name='FotoUpdate'),

]