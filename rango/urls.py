# script for handling urls for the rango app

# Andrew Partridge
# 18/01/2019

from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# above imports relevant Django machinery for URL mappings
# and thew views module from rango. This allows the calling
# of function url and point to the index view for the mapping
# in urlpatterns 