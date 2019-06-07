from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('ootd/', views.ootd, name='upload'),
    path('like/<int:post_id>', views.like, name='like'),
    # path('weather/<str:x>/<str:y>', views.weather, name='weather'),
]
