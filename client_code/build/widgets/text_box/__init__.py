from ._anvil_designer import text_boxTemplate


class text_box(text_boxTemplate):
    def __init__(self, section, **properties):
        self.init_components(**properties)

        self.tag.logic = None
        # self.tag.visible=True

        from ..toolbar import toolbar

        toolbar = toolbar(align="left", section=section, parent=self)
        self.add_component(toolbar)
