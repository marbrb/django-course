from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home1, name='home'),
    path('hide/', views.redirect1),
    path('<int:id>/', views.example1),
    path('<int:id>/<slug:name>/', views.example2),
]




# str - Matches any non-empty string, excluding the path separator, '/'.
# str is default

# int - Matches zero or any positive integer. Returns an int.
# slug - Matches any slug string consisting of ASCII letters or numbers, plus the dash and underscore characters
# uuid - Matches a formatted UUID. 075194d3-6885-417e-a8a8-6c931e272f00
# path - Matches any non-empty string, including the path separator, '/'.
