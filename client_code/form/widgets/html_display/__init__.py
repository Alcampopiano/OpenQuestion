from ._anvil_designer import html_displayTemplate


class html_display(html_displayTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
