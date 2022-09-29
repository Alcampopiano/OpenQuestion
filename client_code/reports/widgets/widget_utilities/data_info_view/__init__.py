import anvil.server

from ._anvil_designer import data_info_viewTemplate


class data_info_view(data_info_viewTemplate):
    def __init__(self, data_dicts, **properties):
        self.init_components(**properties)

        html = anvil.server.call("data_dicts_to_html", data_dicts)
        self.html = html
