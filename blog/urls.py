
from django.conf.urls import include, url
from django.urls import path
from blog.views import index, home, haha

urlpatterns = [
    url(r'^index/$',index, name='index'),
    url(r'^home/$',home, name='home'),
    url(r'^haha/$',haha, name='haha'),
]
