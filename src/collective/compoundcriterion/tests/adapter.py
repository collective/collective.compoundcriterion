# encoding: utf-8

from collective.compoundcriterion.tests.test_criterion import TEXT_TO_FIND


class CompoundCrietrionFilterAdapter(object):

    def __init__(self, context):
        self.context = context

    @property
    def query(self):
        return {'Title': {'query': TEXT_TO_FIND}}
