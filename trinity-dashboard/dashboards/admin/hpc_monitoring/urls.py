from django.conf.urls import patterns
from django.conf.urls import url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^data_tl$', views.DataViewTL.as_view(), name='data_tl'),
    url(r'^data_tr$', views.DataViewTR.as_view(), name='data_tr'),
    url(r'^data_bl$', views.DataViewBL.as_view(), name='data_bl'),
    url(r'^data_br$', views.DataViewBR.as_view(), name='data_br'),
)
