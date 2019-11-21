from django.conf.urls import include
from django.urls import re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('artist', views.ArtistView)
router.register('song', views.SongView)

urlpatterns = [
    re_path('', include(router.urls))
]
