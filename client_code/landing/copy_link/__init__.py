from ._anvil_designer import copy_linkTemplate
from anvil import *
import anvil.server
import anvil.microsoft.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class copy_link(copy_linkTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def copy_click(self, text_to_copy, **event_args):
    
    self.call_js("copyclip", text_to_copy)
    #self.label_1.visible=True

