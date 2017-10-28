from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cursos_list, name='cursos_list'),
]
