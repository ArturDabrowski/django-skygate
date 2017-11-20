from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth.views import logout
from rest_framework.urlpatterns import format_suffix_patterns
from SkyGate import views

app_name = 'SkyGate'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'object/add/$', views.ExampleModelCreate.as_view(), name='object-add'),
    url(r'object/(?P<pk>[0-9]+)/$', views.ExampleModelUpdate.as_view(), name='object-update'),
    url(r'object/(?P<pk>[0-9]+)/delete/$', views.ExampleModelDelete.as_view(), name='object-delete'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^objects/$', views.ExampleModelList.as_view(), name='objects')

]

urlpatterns = format_suffix_patterns(urlpatterns)




