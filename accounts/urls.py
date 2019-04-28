from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/',views.profile),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]