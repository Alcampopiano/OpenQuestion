import anvil

from ._anvil_designer import select_action_reportTemplate


class select_action_report(select_action_reportTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        rows = anvil.server.call("get_reports")
        self.repeating_panel_reports.items = rows

    def new_report_click(self, **event_args):
        """This method is called when the button is clicked"""
        anvil.open_form("reports.main")

    def form_show(self, **event_args):

        for i, comp in enumerate(self.repeating_panel_reports.get_components()):

            if not i % 2:
                comp.background = "theme:Gray 100"

            else:
                comp.background = "white"

    def link_home_click(self, **event_args):
        anvil.open_form("landing.main")
