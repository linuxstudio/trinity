from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables
from horizon.utils import memoized
from horizon import workflows

from  . import tables as hardware_tables
from  . import workflows as hardware_workflows



class IndexView(tables.DataTableView):
  table_class=hardware_tables.HardwareTable
  template_name='project/hpc_hardware/index.html'

  def get_data(self):
    return []

