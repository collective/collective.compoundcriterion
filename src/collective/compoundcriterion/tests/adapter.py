# encoding: utf-8


class CompoundCrietrionFilterAdapter(object):

    def __init__(self, context):
        self.context = context

    @property
    def query(self):
        return {'Title': {'query': u'special_text_to_find'}}
