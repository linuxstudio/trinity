from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.project import dashboard


class Environment(horizon.Panel):
    name = _("Environment")
    slug = 'hpc_environment'


dashboard.Project.register(Environment)
