from ._anvil_designer import nodeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class node(nodeTemplate):
  def __init__(self, node_text, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.link_label.text=node_text

  def node_click(self, **event_args):    
    self.column_panel.visible=(self.column_panel.visible is False)
    
    if self.link_label.icon=='fa:caret-right':
      self.link_label.icon='fa:caret-down'
      
    else:
      self.link_label.icon='fa:caret-right'

