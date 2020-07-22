from ._anvil_designer import propertiesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class properties(propertiesTemplate):
  def __init__(self, prop_text, spec_comp, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_prop.text=prop_text
    self.column_panel.add_component(spec_comp)
    
    
  