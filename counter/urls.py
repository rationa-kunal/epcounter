from django.conf.urls import include, url
from . import views as counter_views

urlpatterns = [
    url(r'complete_serial/(?P<serial_id>[0-9]+)$', counter_views.complete_serial, name='complete_serial'),
    url(r'edit_serial/(?P<serial_id>[0-9]+)$', counter_views.edit_serial, name='edit_serial'),
    url(r'inc_season/(?P<serial_id>[0-9]+)$', counter_views.inc_season, name='inc_season'),
    url(r'dec_season/(?P<serial_id>[0-9]+)$', counter_views.dec_season, name='dec_season'),
    url(r'inc_counter/(?P<serial_id>[0-9]+)$', counter_views.inc_counter, name='inc_counter'),
    url(r'dec_counter/(?P<serial_id>[0-9]+)$', counter_views.dec_counter, name='dec_counter'),
    url(r'add_serial/$', counter_views.add_serial, name='add_serial'),
    url(r'$', counter_views.list_serial, name='list_serial'),
]
