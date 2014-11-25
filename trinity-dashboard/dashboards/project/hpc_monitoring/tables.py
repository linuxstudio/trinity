from django.utils.translation import ugettext_lazy as _

from horizon import tables


class MonitoringTable(tables.DataTable):
    nodes=tables.Column("nodes", verbose_name=_("Node group"))
    status=tables.Column("status",verbose_name=_("Status"))

    class Meta:
        name = "hpc_monitoring"
        verbose_name = _("HPC monitoring info ")
