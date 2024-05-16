from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_list_create, name='poll_list_create'),
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('<int:poll_id>/agree/', views.vote_agree, name='vote_agree'),
    path('<int:poll_id>/disagree/', views.vote_disagree, name='vote_disagree'),
]
