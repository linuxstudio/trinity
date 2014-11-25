from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables
from horizon.utils import memoized
from horizon import workflows

from  . import tables as clusters_tables
from  . import workflows as clusters_workflows



class IndexView(tables.DataTableView):
  table_class=clusters_tables.ClustersTable
  template_name='admin/hpc_clusters/index.html'

  def get_data(self):
    return []


class CreateClusterView(workflows.WorkflowView):
  workflow_class = clusters_workflows.CreateCluster

class UpdateClusterView(workflows.WorkflowView):
  workflow_class = clusters_workflows.UpdateCluster
