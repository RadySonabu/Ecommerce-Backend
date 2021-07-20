
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api.my_user import MyUserView
from .api.register import RegisterApi

router = DefaultRouter()

router.register("my-user", MyUserView)


urlpatterns = [
    path("", include("rest_framework.urls")),
    path("", include(router.urls)),
    path('register/', RegisterApi.as_view(), name='register'),
]