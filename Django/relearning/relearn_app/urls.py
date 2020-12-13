from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('bears/<str:str_val>', views.second_page),	   
    path('redirected_route', views.you_redirected),
    path('users', views.handlePost),
    path('success', views.success)
]