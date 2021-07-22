from django.urls import path

from app import views

urlpatterns = [
    path('home', views.index, name = 'home'),
    path('create', views.create, name = 'create'),
    path('vote/<poll_id>/', views.vote, name = 'vote'),
    path('results/<poll_id>/', views.results, name = 'results')
]
