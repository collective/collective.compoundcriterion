# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.compoundcriterion import HAS_PLONE_5_AND_MORE
from collective.compoundcriterion.testing import IntegrationTestCase
from plone import api

if HAS_PLONE_5_AND_MORE:
    from Products.CMFPlone.utils import get_installer


class TestInstall(IntegrationTestCase):
    """Test installation of collective.compoundcriterion into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if not HAS_PLONE_5_AND_MORE:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        else:
            self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if collective.compoundcriterion is installed with portal_quickinstaller."""
        if not HAS_PLONE_5_AND_MORE:
            self.assertTrue(self.installer.isProductInstalled('collective.compoundcriterion'))
        else:
            self.assertTrue(self.installer.is_product_installed('collective.compoundcriterion'))        
        
    def test_uninstall(self):
        """Test if collective.compoundcriterion is cleanly uninstalled."""
        if not HAS_PLONE_5_AND_MORE:
            self.installer.uninstallProducts(['collective.compoundcriterion'])
            self.assertFalse(self.installer.isProductInstalled('collective.compoundcriterion'))
        else:
            self.installer.uninstall_product('collective.compoundcriterion')
            self.assertFalse(self.installer.is_product_installed('collective.compoundcriterion'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollectiveCompoundcriterionLayer is registered."""
        from collective.compoundcriterion.interfaces import ICollectiveCompoundcriterionLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveCompoundcriterionLayer, utils.registered_layers())
