from ._anvil_designer import check_boxTemplate


class check_box(check_boxTemplate):
    def __init__(self, section, **properties):
        self.init_components(**properties)

        self.tag.logic = None
        # self.tag.visible=True

        from ..toolbar import toolbar

        toolbar = toolbar(align="left", section=section, parent=self)

        self.add_component(toolbar)
