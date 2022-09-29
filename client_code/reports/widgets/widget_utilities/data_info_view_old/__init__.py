import anvil.server

from ._anvil_designer import data_info_view_oldTemplate


class data_info_view_old(data_info_view_oldTemplate):
    def __init__(self, data_dicts, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        html = anvil.server.call("data_dicts_to_html", data_dicts)
        self.html = html
        # self.markdown_display.html=html
