from ._anvil_designer import dateTemplate


class date(dateTemplate):
    def __init__(self, section, **properties):
        self.init_components(**properties)

        self.tag.logic = None
        # self.tag.visible=True

        from ..toolbar import toolbar

        toolbar = toolbar(align="left", section=section, parent=self)
        self.add_component(toolbar)
