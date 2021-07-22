
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api.product import ProductView

router = DefaultRouter()

router.register("product", ProductView)


urlpatterns = [path("", include("rest_framework.urls")),path("", include(router.urls)),]