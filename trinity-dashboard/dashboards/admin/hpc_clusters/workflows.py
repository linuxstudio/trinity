from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import messages
from horizon import workflows


class AllocateAction(workflows.Action):
  hpc_enabled     = forms.BooleanField(label=_("Allocate HPC resources to this project"),
                         required=True, initial=False)
  hpc_description = forms.CharField   (label=_("Description"),
                         widget=forms.widgets.Textarea(), required=False)
  hpc_default     = forms.BooleanField(label=_("Boot with default configuration?"),
                         required=True, initial=False)
  hpc_login       = forms.IntegerField(label=_("Number of login nodes"),
                         min_value=1)
  hpc_compute     = forms.IntegerField(label=_("Generic compute nodes"),
                         min_value=0)
  hpc_gpu         = forms.IntegerField(label=_("GPU enabled nodes"),
                         min_value=0)
  hpc_highmem     = forms.IntegerField(label=_("High memory nodes"),
                         min_value=0)
  
  class Meta:
    name = _("HPC Resources")
    help_text = _("From here you can allocate  "
                    "HPC resources to your project.")


class AllocateStep(workflows.Step):
  action_class = AllocateAction
  contributes = ("hpc_enabled",
                 "hpc_description",
                 "hpc_default",
                 "hpc_login",
                 "hpc_compute",
                 "hpc_gpu",
                 "hpc_highmem",)



class CreateCluster(workflows.Workflow):
  slug = "create_cluster"
  name = _("Create Cluster")
  finalize_button_name = _("Create Cluster")
  success_message = _('Created new cluster')
  failure_message = _('Unable to create cluster')
  success_url = "horizon:admin:hpc_clusters:index"
  default_steps = (AllocateStep,)


class UpdateCluster(workflows.Workflow):
  slug = "update_cluster"
  name = _("Update Cluster")
  finalize_button_name = _("Save Changes")
  success_message = _('Cluster updated')
  failure_message = _('Unable to make requested changes')
  success_url = "horizon:admin:hpc_clusters:index"
  default_steps = (AllocateStep,)

