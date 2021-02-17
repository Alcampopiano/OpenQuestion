from ._anvil_designer import data_info_viewTemplate
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
from ... import widget_utilities

class data_info_view(data_info_viewTemplate):
  def __init__(self, data_dicts, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    html=anvil.server.call('data_dicts_to_html',data_dicts)
    self.markdown_display.html=html