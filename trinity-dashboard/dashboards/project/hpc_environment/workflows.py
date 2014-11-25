from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import messages
from horizon import workflows



class ModifyAction(workflows.Action):
    hpc_osystem     = forms.ChoiceField(label=_("Operating System"),
                           required=True, 
                           choices=[('centos','CentOS'),('rhel', 'RedHat Enterprise Linux'),('ubuntu','Ubuntu')])
    hpc_scheduler   = forms.ChoiceField (label=_("Resource Manager/Scheduler"),
                           required=True,
                           choices=[('slurm','SLURM'), ('torque','MOAB/TORQUE')])
    hpc_monitor     = forms.ChoiceField(label=_("Monitoring system"),
                           required=True, 
                           choices=[('ganglia','Ganglia')])
    
    class Meta:
        name = _("HPC Environment Configuration")
        help_text = _("From here you can edit "
                      "the configuration of you HPC environment")


class ModifyStep(workflows.Step):
    action_class = ModifyAction
    contributes = ("hpc_osystem",
                   "hpc_scheduler",
                   "hpc_monitor",)



class ModifyWorkflow(workflows.Workflow):
    slug = "hpc_modify"
    name = _("Modify HPC environment")
    finalize_button_name = _("Update environment")
    success_message = _('Environment update successful')
    failure_message = _('Environment update unsuccessful')
    success_url = "horizon:project:hpc_environment:index"
    default_steps = (ModifyStep,)

