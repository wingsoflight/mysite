from django.conf.urls import url
from . import views

urlpatterns = [
    # /video/
    url(r'^$', views.index, name='index'),
]