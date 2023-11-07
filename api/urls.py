from django.urls import path 
from . import views
urlpatterns = [
    path('register/', views.post),
    path('login/' , views.Login)
]
