from ._anvil_designer import text_areaTemplate


class text_area(text_areaTemplate):
    def __init__(self, section, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.tag.logic = None
        # self.tag.visible=True

        from ..toolbar import toolbar

        toolbar = toolbar(align="left", section=section, parent=self)
        self.add_component(toolbar)
