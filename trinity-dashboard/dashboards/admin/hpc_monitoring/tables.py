from django.utils.translation import ugettext_lazy as _

from horizon import tables


def get_type(datum):
  return datum.type

def get_amount(datum):
  return datum.amount

class OverviewTable(tables.DataTable):
#  The first argument in the Column instance creator (the 'transform')
#  is either an attribute of a single item of the iterable 'data' (--> the 
# return value of get_data from the views module) or it can be  the return
# value of a callable.

    type=tables.Column(get_type, verbose_name=_("Type"))
    amount=tables.Column(get_amount,verbose_name=_("Amount"))
 
    def get_object_id(self,datum):
      return datum.type

    class Meta:
        name = "hpc_overview"
        verbose_name = _("HPC overview ")

