from ._anvil_designer import survey_rowTemplate
import anvil
import anvil.server
from ...copy_link import copy_link


class survey_row(survey_rowTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.label_title.text = self.item["title"]
        self.button_build.tag.row = self.item

    def button_build_form_click(self, **event_args):

        with anvil.Notification("", title="please wait..."):
            row = self.button_build.tag.row
            anvil.open_form("build.main", row=row)

    def data_click(self, **event_args):

        row = self.button_build.tag.row

        if row["submissions"]:
            anvil.download(row["submissions"])

        else:
            anvil.Notification("", title="No data to anvil.download just yet!").show()

    def share_click(self, **event_args):

        form_id = self.button_build.tag.row["form_id"]
        app_url = anvil.server.get_app_origin() + "#?" + "form_id=" + form_id
        content = copy_link()
        content.copy_click(app_url)
        anvil.Notification(
            "Share this link or paste it in the browser", title="Link copied!"
        ).show()

    def settings_click(self, **event_args):
        row = self.button_build.tag.row
        anvil.open_form("landing.settings.survey_settings", row)

    def button_chart_click(self, **event_args):

        with anvil.Notification("", title="please wait..."):
            row = self.button_build.tag.row
            anvil.open_form("reports.main", row=row)
