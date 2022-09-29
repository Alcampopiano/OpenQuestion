import anvil.server

from ._anvil_designer import edit_templatesUNUSEDTemplate


class edit_templatesUNUSED(edit_templatesUNUSEDTemplate):
    def __init__(self, vl_schema, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # self.tag.vl_schema=vl_schema

        # Any code you write here will run when the form opens.
        rows = anvil.server.call("get_templates")
        self.repeating_panel_1.items = rows
