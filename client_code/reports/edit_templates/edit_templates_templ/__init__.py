from ._anvil_designer import edit_templates_templTemplate
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

class edit_templates_templ(edit_templates_templTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.image.source=self.item['images'].url
    #self.json.tag.spec=self.item['templates']

  def button_delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
  
  def form_show(self, **event_args):
    spec=self.item['templates']
    self.json.set_json_editor(spec)

