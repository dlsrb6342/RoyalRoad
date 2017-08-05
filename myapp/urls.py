from django.conf.urls import url
from myapp.views import *

urlpatterns = [
	url(r'^/$', MainView.as_view(), name='main')
    url(r'^data/$', DataView.as_view(), name='data'),
    url(r'^auto/$', SearchView.as_view(), name='search'),
]
