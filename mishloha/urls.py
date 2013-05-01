from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'main.views.home'),
    url(r'^details/(?P<cust_id>\d+)/$', 'main.views.details'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)