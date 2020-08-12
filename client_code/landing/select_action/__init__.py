from ._anvil_designer import select_actionTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class select_action(select_actionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    rows=anvil.server.call('get_forms')
    self.repeating_panel_1.items=rows
    
    rows=anvil.server.call("get_reports")
    self.repeating_panel_2.items=rows
    

  def new_survey_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('build.main')

  def new_report_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('reports.main')

  def form_show(self, **event_args):
            
    for i, comp in enumerate(self.repeating_panel_1.get_components()):

      if not i%2:
        comp.background='theme:Gray 100'
        
      else:
        comp.background='white'
        

    for i, comp in enumerate(self.repeating_panel_2.get_components()):

      if not i%2:
        comp.background='theme:Gray 100'
        
      else:
        comp.background='white'





