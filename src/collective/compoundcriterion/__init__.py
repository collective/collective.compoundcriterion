# -*- coding: utf-8 -*-
"""Init and utils."""

from plone import api
from zope.i18nmessageid import MessageFactory

HAS_PLONE_5_AND_MORE = int(api.env.plone_version()[0]) >= 5

_ = MessageFactory('collective.compoundcriterion')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
