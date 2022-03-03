from django.urls import path

from .views import index, profile

app_name = "profiles"
urlpatterns = [
    path('profiles/', index, name='index'),
    path('profiles/<str:username>/', profile, name='profile'),
]
