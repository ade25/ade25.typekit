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
    useLoadCallback = schema.Bool(
        title=_(u"Use callback to defer javascript loading?"),
        description=_(u"This settings allows to register javascript that "
                      u"manipulates the DOM for a dedicated callback function "
                      u"that is triggered when font loading has completed."),
        default=False,
        required=False,
    )
