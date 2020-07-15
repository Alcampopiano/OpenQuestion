from ._anvil_designer import radio_buttonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class radio_button(radio_buttonTemplate):
  def __init__(self, options, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.tag.logic=None
    self.tag.logic_target_ids=[]

    # Any code you write here will run when the form opens.
    for op in options:
      b=RadioButton(text=op, foreground='black')
      b.group_name='group'
      self.column_panel.add_component(b)