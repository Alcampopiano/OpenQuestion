from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
import anvil.microsoft.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class main(mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

#     # Any code you write here will run when the form opens.
#     while not anvil.users.login_with_form():
#       pass

  def button_survey_click(self, **event_args):
      open_form('landing.select_action_survey')
      
  def buttons_reports_click(self, **event_args):
      open_form('landing.select_action_report')


