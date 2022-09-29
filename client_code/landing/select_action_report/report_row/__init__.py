import anvil

from ._anvil_designer import report_rowTemplate


class report_row(report_rowTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

        self.label_title.text = self.item["title"]
        self.button_build.tag.row = self.item

    def button_build_click(self, **event_args):

        print(" this context manager is not working for some reason")
        with anvil.Notification("", title="please wait..."):
            row = self.button_build.tag.row
            anvil.open_form("reports.main", row=row)

    def download_click(self, **event_args):
        anvil.Notification(
            "should anvil.download the html report", title="not yet implemented"
        ).show()

    def button_settings_click(self, **event_args):
        row = self.button_build.tag.row
        anvil.open_form("landing.settings.report_settings", row)
