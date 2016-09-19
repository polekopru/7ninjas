from django.conf.urls import url, include
from django.contrib import admin
import ninjas.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', ninjas.views.index),
    url(r'^accounts/signup/$', ninjas.views.signup),
    url(r'^account/logged/$', ninjas.views.logged_in),
]
