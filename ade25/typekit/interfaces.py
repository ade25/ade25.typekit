from zope import schema
from zope.interface import Interface

from ade25.typekit import MessageFactory as _


class IAde25TypeKit(Interface):
    """ A marker inteface for a specific theme layer """


class ITypeKitSettings(Interface):
    """ Settings schema """
    kitID = schema.TextLine(
        title=_(u"TypeKit Kit ID"),
        required=True,
    )
