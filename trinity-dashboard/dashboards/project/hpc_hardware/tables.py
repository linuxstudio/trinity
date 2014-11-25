from django.utils.translation import ugettext_lazy as _

from horizon import tables

class HardwareTable(tables.DataTable):
    type=tables.Column("type", verbose_name=_("Type"))
    amount=tables.Column("amount",verbose_name=_("Amount"))

    class Meta:
        name = "hpc_hardware"
        verbose_name = _("Overview of the HPC hardware ")

