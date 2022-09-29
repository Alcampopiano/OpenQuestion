import anvil

from ._anvil_designer import mainTemplate


class main(mainTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    #     while not anvil.users.login_with_form():
    #       pass

    def button_survey_click(self, **event_args):
        anvil.open_form("landing.select_action_survey")

    def buttons_reports_click(self, **event_args):
        anvil.open_form("landing.select_action_report")
