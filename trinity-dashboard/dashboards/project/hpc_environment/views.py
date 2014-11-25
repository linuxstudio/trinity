from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables
from horizon.utils import memoized
from horizon import workflows

from . import tables as environment_tables
from . import workflows as environment_workflows


class IndexView(tables.DataTableView):
  table_class = environment_tables.EnvironmentTable
  template_name = 'project/hpc_environment/index.html'

  def get_data(self):
    return []


class ModifyView(workflows.WorkflowView):
  workflow_class = environment_workflows.ModifyWorkflow


