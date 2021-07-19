from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('commision_calculator.urls')),
    path('admin/', admin.site.urls),
]
