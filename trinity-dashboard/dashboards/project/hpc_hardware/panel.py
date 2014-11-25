from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.project import dashboard


class Hardware(horizon.Panel):
    name = _("Hardware")
    slug = 'hpc_hardware'


dashboard.Project.register(Hardware)
