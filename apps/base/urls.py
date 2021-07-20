from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.user.urls')),
]
