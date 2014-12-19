from trinityclient import client as trinity_client 
#from trinityclient import test as trinity_client

def trinityclient(request):
  c = trinity_client.Client(username=request.user.username,
                            token=request.user.token.id,
                            tenant=request.user.tenant_name)
  return c


class DictToObject(object):
  def __init__(self,keys,dict,default_keys=[],default_value=None):
    if default_keys:
      for key in default_keys:
        setattr(self,key,dict[key])
    for key in keys:
      if key in dict:
        value=dict[key]
      else:
        value=default_value
      setattr(self,key,value)

def overview(request):
  c=trinityclient(request)
  hardwares_list=c.hardwares_list()
  clusters_detail=c.clusters_detail()
  data=[]
  for cluster in clusters_detail:
    datum=DictToObject(hardwares_list,cluster,default_keys=['cluster'],default_value=0)
    data.append(datum)
  return data  
  
def hardwares_list(request):
  c=trinityclient(request)
  data=c.hardwares_list()
  return data
   
def hardwares_detail(request):
  c=trinityclient(request)
  data=c.hardwares_detail()
  return data  

def cluster_hardware(request,cluster=None):
  c=trinityclient(request)
  if not cluster:
    cluster=request.user.tenant_name
  hardwares=c.cluster_hardware(cluster)
  data=[]
  for hardware in hardwares:
    datum=type('ClusterHardware',(object,),hardware)
    data.append(datum)
  return data  
 
def cluster_modify(request,data):
  c=trinityclient(request)
  cluster=data['name']
  unused_keys=['name','login','description']
  specs={}
  for key,value in data.items():
    if key not in unused_keys:
      specs[key] = value
  modify=c.cluster_modify(cluster,specs)
  return modify['status_ok']
 
def cluster_config(request):
  c=trinityclient(request)
  cluster=request.user.tenant_name
  config=c.cluster_config(cluster)
  data=[]
  for option in config:
    datum=type('ClusterConfig', (object,),option)
    data.append(datum)
  return data 

def load_per_proc(request):
  c=trinityclient(request)
  load=[]
#  load=c.load_per_proc()
  return load

def cpu_usage(request):
  c=trinityclient(request)
  usage=[]
#  usage=c.cpu_usage()
  return usage

def disk_usage(request):
  c=trinityclient(request)
  usage=[]
#  usage=c.disk_usage()
  return usage

def byte_transfer(request):
  c=trinityclient(request)
  rate=[]
#  rate=c.byte_transfer()
  return rate


