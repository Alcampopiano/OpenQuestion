from ._anvil_designer import select_action_surveyTemplate
from anvil import *
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class select_action_survey(select_action_surveyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    rows=anvil.server.call('get_forms')
    self.repeating_panel_surveys.items=rows
    

  def new_survey_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('build.main')


  def form_show(self, **event_args):
            
    for i, comp in enumerate(self.repeating_panel_surveys.get_components()):

      if not i%2:
        comp.background='theme:Gray 100'
        
      else:
        comp.background='white'

#   def link_home_click(self, **event_args):
#     #open_form('landing.main')





