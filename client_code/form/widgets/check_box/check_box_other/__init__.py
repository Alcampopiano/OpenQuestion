from ._anvil_designer import check_box_otherTemplate
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

class check_box_other(check_box_otherTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def check_box_change(self, **event_args):

    if self.check_box.checked:
      self.spacer.visible=True
      self.text_box.visible=True
    
    else:
      self.text_box.text=''
      self.spacer.visible=False
      self.text_box.visible=False
      

