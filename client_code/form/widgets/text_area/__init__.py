from ._anvil_designer import text_areaTemplate


class text_area(text_areaTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

        self.tag.logic = None
