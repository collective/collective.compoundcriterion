# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.compoundcriterion.interfaces import ICollectiveCompoundcriterionLayer
from collective.compoundcriterion.testing import IntegrationTestCase
from plone.base.utils import get_installer
from plone.browserlayer import utils
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.i18n import translate
from zope.i18nmessageid import Message


FIELD = "plone.app.querystring.field.CompoundCriterion"
OPERATION = "plone.app.querystring.operation.compound.is"


class TestInstall(IntegrationTestCase):
    """Test installation of collective.compoundcriterion into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if collective.compoundcriterion is installed."""
        self.assertTrue(
            self.installer.is_product_installed("collective.compoundcriterion")
        )

    def test_uninstall(self):
        """Test if collective.compoundcriterion is cleanly uninstalled."""
        self.installer.uninstall_product("collective.compoundcriterion")
        self.assertFalse(
            self.installer.is_product_installed("collective.compoundcriterion")
        )

    def test_uninstall_profile(self):
        """The uninstall profile removes the browser layer and the registry records."""
        self.installer.uninstall_product("collective.compoundcriterion")
        self.assertNotIn(ICollectiveCompoundcriterionLayer, utils.registered_layers())
        records = getUtility(IRegistry).records
        self.assertEqual(
            [name for name in records.keys() if name.startswith((FIELD, OPERATION))], []
        )

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollectiveCompoundcriterionLayer is registered."""
        self.assertIn(ICollectiveCompoundcriterionLayer, utils.registered_layers())

    # registry.xml
    def test_registry(self):
        """The "Compound criterion" field and its "Is" operation are offered by the query widget."""
        registry = getUtility(IRegistry)
        self.assertEqual(registry[FIELD + ".title"], "Compound criterion")
        self.assertEqual(
            registry[FIELD + ".description"],
            "Select the method that will compute the query",
        )
        self.assertEqual(registry[FIELD + ".group"], "Other")
        self.assertEqual(
            registry[FIELD + ".vocabulary"], "collective.compoundcriterion.Filters"
        )
        self.assertEqual(registry[FIELD + ".operations"], [OPERATION])
        self.assertFalse(registry[FIELD + ".sortable"])
        self.assertTrue(registry[FIELD + ".enabled"])
        self.assertEqual(registry[OPERATION + ".title"], "Is")
        self.assertEqual(registry[OPERATION + ".widget"], "MultipleSelectionWidget")
        self.assertEqual(
            registry[OPERATION + ".operation"],
            "collective.compoundcriterion.queryparser._filter_is",
        )
        # titles are i18n messages, translated when the query widget reads the registry
        titles = [
            registry[name]
            for name in (
                FIELD + ".title",
                FIELD + ".description",
                FIELD + ".group",
                OPERATION + ".title",
            )
        ]
        self.assertTrue(all(isinstance(title, Message) for title in titles))
        self.assertEqual(
            [translate(title, target_language="fr") for title in titles],
            [
                "Filtre",
                "Sélectionnez la méthode qui va calculer la requête",
                "Autre",
                "Est",
            ],
        )
