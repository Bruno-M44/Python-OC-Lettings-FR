from django.contrib import admin
from django.urls import path, include

from .views import index

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error)
]
