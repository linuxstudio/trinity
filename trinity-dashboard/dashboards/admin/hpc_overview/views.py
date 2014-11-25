from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables
from horizon.utils import memoized
from horizon import workflows

from  . import tables as overview_tables
#from  . import workflows as overview_workflows



class IndexView(tables.DataTableView):
  table_class=overview_tables.OverviewTable
  template_name='admin/hpc_overview/index.html'

  def get_data(self):
    return []

