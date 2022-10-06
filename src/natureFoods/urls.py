from xml.etree.ElementInclude import include
from django.urls import path, include

from .views import fruitViewSet, vegetalViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register('fruits', fruitViewSet)
router.register('vegetals', vegetalViewSet)

urlpatterns = [
    path('', include(router.urls))
]