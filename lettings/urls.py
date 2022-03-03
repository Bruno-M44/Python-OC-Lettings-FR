from django.urls import path
from .views import index, letting

app_name = "lettings"
urlpatterns = [
    path('lettings/', index, name='index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
]
