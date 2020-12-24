from django.urls import path
from myapp.views import Users
urlpatterns = [
    path('users', Users.as_view(), name="users"),
]
