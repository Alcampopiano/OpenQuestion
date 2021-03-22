from ._anvil_designer import edit_templatesUNUSEDTemplate
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import vega


class edit_templatesUNUSED(edit_templatesUNUSEDTemplate):
  def __init__(self, vl_schema, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.tag.vl_schema=vl_schema

    # Any code you write here will run when the form opens.
    rows=anvil.server.call('get_templates')
    self.repeating_panel_1.items=rows
    
    