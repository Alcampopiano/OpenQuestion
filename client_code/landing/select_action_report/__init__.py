from ._anvil_designer import select_action_reportTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.microsoft.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class select_action_report(select_action_reportTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    rows=anvil.server.call("get_reports")
    self.repeating_panel_reports.items=rows

  def new_report_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('reports.main')

  def form_show(self, **event_args):
            
    for i, comp in enumerate(self.repeating_panel_reports.get_components()):

      if not i%2:
        comp.background='theme:Gray 100'
        
      else:
        comp.background='white'
        
  def link_home_click(self, **event_args):
    open_form('landing.main')

