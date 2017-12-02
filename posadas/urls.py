from django.conf.urls import url
from posadas.views import ListGenericPosada,DetailGenericPosada

urlpatterns = [
    url(r'^posadas/$', ListGenericPosada.as_view(), name="listPosadas"),
    url(r'^posadas/(?P<pk>[0-9]+)/$',DetailGenericPosada.as_view(), name="detailPosada"),
]