import json

from django.http import HttpResponse 
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables
from horizon.utils import memoized
from horizon import workflows

from openstack_dashboard.api import trinity
from  . import tables as monitoring_tables
#from  . import workflows as monitoring_workflows



class Dummy(object):
  pass


class IndexView(TemplateView):
  template_name='admin/hpc_monitoring/index.html'

#  def get(self,request,*args,**kwargs):
#    ret={}
#    return HttpResponse(json.dumps(ret),content_type='application/json')
  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    request=self.request
#    series= [{
#                "data": [ { "x": 0, "y": 40 }, { "x": 1, "y": 49 }],
#                "color": "steelblue"
#        }, {
#                "data": [ { "x": 0, "y": 20 }, { "x": 1, "y": 24 }],
#                "color": "lightblue"
#        }]
#
    series=trinity.load_per_proc(request)
    context.update({"data_tl":json.dumps(series)})
    series=trinity.cpu_usage(request)
    context.update({"data_tr":json.dumps(series)})
    series=trinity.disk_usage(request)
    context.update({"data_bl":json.dumps(series)})
    series=trinity.byte_transfer(request)
    context.update({"data_br":json.dumps(series)})
    

#    context.update({"series" : json.dumps(series)})
    return context

class DataViewTL(TemplateView):
  template_name='admin/hpc_monitoring/data_tl.json'

  def get(self,request,*args,**kwargs):
    series=trinity.load_per_proc(request)
    settings={"auto_size": False}
    ret={"series": series, "settings": settings}
    return HttpResponse(json.dumps(ret),content_type='application/json')

class DataViewTR(TemplateView):
  template_name='admin/hpc_monitoring/data_tr.json'

  def get(self,request,*args,**kwargs):
    series=trinity.cpu_usage(request)
    settings={}
    settings={"auto_size": False}
    ret={"series": series, "settings": settings}
    return HttpResponse(json.dumps(ret),content_type='application/json')

class DataViewBL(TemplateView):
  template_name='admin/hpc_monitoring/data_bl.json'

  def get(self,request,*args,**kwargs):
    series=trinity.disk_usage(request)
    settings={}
    settings={"auto_size": False}
    ret={"series": series, "settings": settings}
    return HttpResponse(json.dumps(ret),content_type='application/json')

class DataViewBR(TemplateView):
  template_name='admin/hpc_monitoring/data_br.json'

  def get(self,request,*args,**kwargs):
    series=trinity.byte_transfer(request)
    settings={}
    settings={"auto_size": False}
    ret={"series": series, "settings": settings}
    return HttpResponse(json.dumps(ret),content_type='application/json')



