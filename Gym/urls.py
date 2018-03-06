from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name="Gym"

urlpatterns = [
    url(r'^', include('core.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^profile/', include('account.urls', namespace="myaccount")),
    url(r'^exercises/', include('exercises.urls', namespace="exercises")),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]
    # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
