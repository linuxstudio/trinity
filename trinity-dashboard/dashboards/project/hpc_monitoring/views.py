from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables
from horizon.utils import memoized
from horizon import workflows

from . import tables as monitoring_tables
#from . import workflows as monitoring_workflows


class IndexView(tables.DataTableView):
    table_class   = monitoring_tables.MonitoringTable
    template_name = 'project/hpc_monitoring/index.html'

    def get_data(self):
        return []

