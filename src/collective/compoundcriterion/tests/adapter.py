class TestingCompoundCriterionFilterAdapter:

    def __init__(self, context):
        self.context = context

    @property
    def query(self):
        return {"Title": {"query": "special_text_to_find"}}


class SampleCompoundCriterionFilterAdapter:

    def __init__(self, context):
        self.context = context

    @property
    def query(self):
        return {"Title": {"query": "title_with_sample_text"}}


class PortalTypeCompoundCriterionFilterAdapter:

    def __init__(self, context):
        self.context = context

    @property
    def query(self):
        return {"portal_type": {"query": ["Document", "Folder"]}}


class WrongFormatCompoundCriterionFilterAdapter:

    def __init__(self, context):
        self.context = context

    @property
    def query(self):
        return {"portal_type": ["Document", "Folder"]}


class NotCompoundCriterionFilterAdapter:

    def __init__(self, context):
        self.context = context

    @property
    def query(self):
        return {"portal_type": {"not": ["Folder"]}}


class WrongNotCompoundCriterionFilterAdapter:

    def __init__(self, context):
        self.context = context

    @property
    def query(self):
        return {"portal_type": {"query": {"not": ["Document"]}}}
