from django.urls import path

from . import views
# app_name para colocar auxiliar a chmar a url ex:polls:detail
# chmar url {% url 'polls:detail' question.id %}

# caso nao tenha colocar o nome no proprio name ex:name='polls_detail'
# chmar url {% url 'polls_detail' question.id %}


urlpatterns = [
    
    #home para  noticia
    path('', views.IndexView.as_view(), name='IndexView'),
  
    #lista os jogos
    path('novo/', views.JogoCreateView.as_view(), name='novo-jogo'),
    path('lista/', views.JogoListView.as_view(), name='JogoListView'),
    path('update/<int:pk>', views.JogoUpdate.as_view(), name='update-jogo'),
    path('delete/<int:pk>', views.JogoDelete.as_view(), name='delete-jogo'),

#

    path('lista-todos-capitulo', views.TodosCapitulosListView.as_view(), name='TodosCapitulosListView'),
    path('lista-todos-jogos', views.AdminJogoListView.as_view(), name='AdminJogoListView'),

    path('novo-capitulo/', views.CapituloCreateView.as_view(), name='CapituloCreateView'),
    path('lista/<int:pk>/', views.CapituloJogoListView.as_view(), name='CapituloJogoListView'),
    path('capitulo/<int:pk>/',views.CapituloJogoDetailView.as_view(), name='CapituloJogoDetailView'),

    path('capitulo-update/<int:pk>', views.CapituloUpdate.as_view(), name='CapituloUpdate'),

    path('delete-capitulo/<int:pk>', views.CapituloDelete.as_view(), name='CapituloDelete'),

   
    
]