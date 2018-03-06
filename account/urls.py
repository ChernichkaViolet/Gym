from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from django.conf.urls import url, include

app_name="Gym"

urlpatterns = [

    path('<int:pk>', views.profile_show, name='profile'),
    # path('<int:pk>/edit/$',  views.profile_update, name='profile_edit'),
    url('^(?P<pk>\d+)/edit$', views.profile_update, name='profile_edit'),
]
