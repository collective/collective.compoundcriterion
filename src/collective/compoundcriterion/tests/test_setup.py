# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.compoundcriterion.interfaces import ICollectiveCompoundcriterionLayer
from collective.compoundcriterion.testing import IntegrationTestCase
from plone import api
from plone.browserlayer import utils
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.utils import getFSVersionTuple
from zope.component import getUtility
from zope.i18n import translate
from zope.i18nmessageid import Message

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:  # Plone 4
    get_installer = None


PLONE_MAJOR = getFSVersionTuple()[0]
FIELD = 'plone.app.querystring.field.CompoundCriterion'
OPERATION = 'plone.app.querystring.operation.compound.is'


class TestInstall(IntegrationTestCase):
    """Test installation of collective.compoundcriterion into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if PLONE_MAJOR < 5:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        else:
            self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if collective.compoundcriterion is installed with portal_quickinstaller."""
        if PLONE_MAJOR < 5:
            self.assertTrue(self.installer.isProductInstalled('collective.compoundcriterion'))
        else:
            self.assertTrue(self.installer.is_product_installed('collective.compoundcriterion'))

    def test_uninstall(self):
        """Test if collective.compoundcriterion is cleanly uninstalled."""
        if PLONE_MAJOR < 5:
            self.installer.uninstallProducts(['collective.compoundcriterion'])
            self.assertFalse(self.installer.isProductInstalled('collective.compoundcriterion'))
        else:
            self.installer.uninstall_product('collective.compoundcriterion')
            self.assertFalse(self.installer.is_product_installed('collective.compoundcriterion'))

    @unittest.skipIf(PLONE_MAJOR < 6, 'uninstall profile registered on Plone 6 only')
    def test_uninstall_profile(self):
        """The uninstall profile removes the browser layer and the registry records."""
        self.installer.uninstall_product('collective.compoundcriterion')
        self.assertNotIn(ICollectiveCompoundcriterionLayer, utils.registered_layers())
        records = getUtility(IRegistry).records
        self.assertEqual([name for name in records.keys() if name.startswith((FIELD, OPERATION))], [])

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollectiveCompoundcriterionLayer is registered."""
        self.assertIn(ICollectiveCompoundcriterionLayer, utils.registered_layers())

    # registry.xml
    def test_registry(self):
        """The "Compound criterion" field and its "Is" operation are offered by the query widget."""
        registry = getUtility(IRegistry)
        self.assertEqual(registry[FIELD + '.title'], u'Compound criterion')
        self.assertEqual(registry[FIELD + '.description'], u'Select the method that will compute the query')
        self.assertEqual(registry[FIELD + '.group'], u'Other')
        self.assertEqual(registry[FIELD + '.vocabulary'], u'collective.compoundcriterion.Filters')
        self.assertEqual(registry[FIELD + '.operations'], [OPERATION])
        self.assertFalse(registry[FIELD + '.sortable'])
        self.assertTrue(registry[FIELD + '.enabled'])
        self.assertEqual(registry[OPERATION + '.title'], u'Is')
        self.assertEqual(registry[OPERATION + '.widget'], u'MultipleSelectionWidget')
        self.assertEqual(registry[OPERATION + '.operation'], u'collective.compoundcriterion.queryparser._filter_is')
        # titles are i18n messages, translated when the query widget reads the registry
        titles = [registry[name] for name in (FIELD + '.title', FIELD + '.description', FIELD + '.group',
                                              OPERATION + '.title')]
        self.assertTrue(all(isinstance(title, Message) for title in titles))
        self.assertEqual(
            [translate(title, target_language='fr') for title in titles],
            [u'Filtre', u'Sélectionnez la méthode qui va calculer la requête', u'Autre', u'Est'])
