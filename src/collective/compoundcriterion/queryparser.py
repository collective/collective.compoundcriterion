# encoding: utf-8

from collective.compoundcriterion.interfaces import ICoumpondCriterionFilter
from zope.component import queryAdapter


def _filter_is(context, row):
    named_adapter = queryAdapter(context,
                                 ICoumpondCriterionFilter,
                                 name=row.values)
    if named_adapter:
        return named_adapter.query
    return {}