from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.admin import dashboard


class Clusters(horizon.Panel):
    name = _("Virtual Clusters")
    slug = 'hpc_clusters'


dashboard.Admin.register(Clusters)
