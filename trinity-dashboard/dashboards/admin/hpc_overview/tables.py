from django.utils.translation import ugettext_lazy as _

from horizon import tables

class OverviewTable(tables.DataTable):
    type=tables.Column("type", verbose_name=_("Type"))
    amount=tables.Column("amount",verbose_name=_("Amount"))

    class Meta:
        name = "hpc_overview"
        verbose_name = _("HPC overview ")

