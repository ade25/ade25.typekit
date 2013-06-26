from five import grok
from Products.CMFCore.interfaces import ISiteRoot

from plone.z3cform import layout
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from ade25.typekit.interfaces import IAde25TypeKit
from ade25.typekit.interfaces import ITypeKitSettings


class TypeKitSettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = ITypeKitSettings
    label = u"TypeKit webfont settings"


class TypeKitSettingsView(grok.View):
    """
        View which wrap the settings form using ControlPanelFormWrapper
        to a HTML boilerplate frame.
    """
    grok.name("typekit-fonts-settings")
    grok.layer(IAde25TypeKit)
    grok.context(ISiteRoot)

    def render(self):
        view_factor = layout.wrap_form(TypeKitSettingsEditForm,
                                       ControlPanelFormWrapper)
        view = view_factor(self.context, self.request)
        return view()
