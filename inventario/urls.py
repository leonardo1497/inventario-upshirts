from django.conf.urls import url
from rest_framework import routers
from inventario.views import *

urlpatterns = [
    url(r'^inventario/$', InventarioView.as_view()),
    url(r'^inventario/(?P<pk>\d+)/?$/', InventarioView.as_view())
]