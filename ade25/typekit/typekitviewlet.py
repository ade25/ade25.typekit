from five import grok
from plone import api
from zope.interface import Interface
from zope.component import getUtility

from plone.registry.interfaces import IRegistry
from plone.app.layout.viewlets.interfaces import IHtmlHead

from ade25.typekit.interfaces import IAde25TypeKit
from ade25.typekit.interfaces import ITypeKitSettings


class TypeKitViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.layer(IAde25TypeKit)
    grok.require('zope2.View')
    grok.viewletmanager(IHtmlHead)
    grok.name('ade25.typekit.TypeKitViewlet')

    def update(self):
        self.available = self.is_available()

    def is_available(self):
        if self.kit_id() is None:
            return False
        return True

    def kit_source_url(self):
        url = '//use.typekit.net/%s.js' % self.kit_id()
        return url

    def kit_id(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ITypeKitSettings)
        kit_id = settings.kitID
        return kit_id
