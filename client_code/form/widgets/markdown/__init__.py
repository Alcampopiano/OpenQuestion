from ._anvil_designer import markdownTemplate


class markdown(markdownTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.tag.logic = None
