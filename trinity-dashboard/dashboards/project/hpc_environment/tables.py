from django.utils.translation import ugettext_lazy as _

from horizon import tables

class ModifyAction(tables.LinkAction):
    name = "modify"
    verbose_name = _("Modify HPC environment")
    url = "horizon:project:hpc_environment:modify"
    classes = ("btn-launch", "ajax-modal")

class EnvironmentTable(tables.DataTable):
    hpc_osystem=tables.Column("osystem", verbose_name=_("Operating system"))
    hpc_scheduler=tables.Column("scheduler",verbose_name=_("Resource manager/Job scheduler"))
    hpc_monitor=tables.Column("monitor",verbose_name=_("Monitoring system"))

    class Meta:
        name = "hpc_environment"
        verbose_name = _("Current HPC configuration")
        table_actions=(ModifyAction,)

