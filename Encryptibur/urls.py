from django.conf.urls import url

from . import views
from. import login

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', login.login, name='login'),
]
