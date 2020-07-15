from ._anvil_designer import dateTemplate
from anvil import *
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


