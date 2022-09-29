from ._anvil_designer import markdown_displayTemplate


class markdown_display(markdown_displayTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
