from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from kolibri.core.webpack import hooks as webpack_hooks
from kolibri.plugins import KolibriPluginBase
from kolibri.plugins.hooks import register_hook
from kolibri.utils import translation
from kolibri.utils.translation import ugettext as _


class Policies(KolibriPluginBase):
    @property
    def url_slug(self):
        return "policies"

    def name(self, lang):
        with translation.override(lang):
            return _("Policies")


@register_hook
class PoliciesAsset(webpack_hooks.WebpackBundleHook):
    print("policies app")
    bundle_id = "app"
