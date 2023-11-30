from collective.compoundcriterion.interfaces import ICompoundCriterionFilter
from Products.CMFPlone import PloneMessageFactory as _p
from zope.component import getGlobalSiteManager
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class CompoundCriterionVocabulary(object):
    """Vocabulary factory for compound criterion.
       This will return every named adapter that provides the ICoumpondCriterionFilter interface."""    

    def __call__(self, context):
        sm = getGlobalSiteManager()
        registrations = [a for a in sm.registeredAdapters() if a.provided == ICompoundCriterionFilter]
        terms = [SimpleTerm(adapter.name, adapter.name, _p(adapter.name)) for adapter in registrations]
        return SimpleVocabulary(terms)


CompoundCriterionVocabularyFactory = CompoundCriterionVocabulary()
