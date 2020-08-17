from ._anvil_designer import markdownTemplate
from anvil import *
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class markdown(markdownTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.tag.logic=None
