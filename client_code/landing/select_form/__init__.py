from ._anvil_designer import select_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class select_form(select_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    rows=anvil.server.call('get_forms')
    self.repeating_panel_1.items=rows
    

  def new_form_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('build.main')

