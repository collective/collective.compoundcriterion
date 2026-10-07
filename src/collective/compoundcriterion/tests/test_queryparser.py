# -*- coding: utf-8 -*-
"""Tests of the "Is" operation of the compound criterion."""

from collective.compoundcriterion.queryparser import _get_real_context
from collective.compoundcriterion.testing import IntegrationTestCase
from plone.app.querystring.queryparser import parseFormquery
from plone.z3cform.layout import FormWrapper
from zope.component import getMultiAdapter


class TestQueryparser(IntegrationTestCase):

    def test_get_real_context(self):
        request = self.layer['request']
        folder = self.portal['folder']
        # Plone site: the context of the published view
        self.assertEqual(_get_real_context(self.portal), self.portal)
        request['PUBLISHED'] = getMultiAdapter((folder, request), name='plone_context_state')
        self.assertEqual(_get_real_context(self.portal), folder)
        # z3c.form wrapper: its context
        self.assertEqual(_get_real_context(FormWrapper(folder, request)), folder)
        # other context: unchanged
        request['PUBLISHED'] = getMultiAdapter((self.portal, request), name='plone_context_state')
        self.assertEqual(_get_real_context(folder), folder)

    def test_filter_is(self):
        # a single value (SingleSelectionWidget) works like a list of one value
        query = [{
            'i': 'CompoundCriterion',
            'o': 'plone.app.querystring.operation.compound.is',
            'v': u'testing-compound-adapter',
        }]
        self.assertEqual(parseFormquery(self.portal, query), {'Title': {'query': u'special_text_to_find'}})
