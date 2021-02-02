from ._anvil_designer import dateTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class date(dateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.tag.logic=None
    self.tag.logic_target_ids=[]
    self.tag.current_value=None

  def date_picker_change(self, **event_args):
    self.tag.current_value=self.date_picker.date
    
    from .... import form
    for target_id in self.tag.logic_target_ids:
      form.check_logic_for_visibility(target_id)


