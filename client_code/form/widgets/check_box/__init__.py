from ._anvil_designer import check_boxTemplate
from anvil import *
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class check_box(check_boxTemplate):
  def __init__(self, options, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.tag.logic=None

    # Any code you write here will run when the form opens.
    for op in options:
      c=CheckBox(text=op, foreground='black')
      self.column_panel.add_component(c)