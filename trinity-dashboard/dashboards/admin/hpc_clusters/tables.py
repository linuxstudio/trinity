from django.utils.translation import ugettext_lazy as _

from horizon import tables

class CreateCluster(tables.LinkAction):
  name = "create"
  verbose_name = _("Create New Cluster")
  url = "horizon:admin:hpc_clusters:create"
  classes = ("btn-launch", "ajax-modal",)

class UpdateCluster(tables.LinkAction):
  name = "update"
  verbose_name = _("Edit Cluster")
  url = "horizon:admin:hpc_clusters:update"
  classes = ("ajax-modal", "btn-edit")


class ClustersTable(tables.DataTable):
  cluster_name=tables.Column("cluster_name", verbose_name=_("Name"))
  project_id  =tables.Column("project_id",verbose_name=_("Project ID"))
    

  class Meta:
    name = "hpc_clusters"
    verbose_name = _("Virtual HPC Clusters ")
    row_actions = (UpdateCluster,)
    table_actions = (CreateCluster,)    
