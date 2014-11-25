from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.project import dashboard


class Monitoring(horizon.Panel):
    name = _("Monitoring")
    slug = 'hpc_monitoring'


dashboard.Project.register(Monitoring)
