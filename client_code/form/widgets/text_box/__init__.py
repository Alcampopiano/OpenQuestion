from ._anvil_designer import text_boxTemplate
from anvil import *
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class text_box(text_boxTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)

    self.tag.logic=None
    self.tag.logic_target_ids=[]
    self.tag.current_value=None

  def text_box_change(self, **event_args):
    
    if type(self.text_box.text) is not str:
      self.tag.current_value=self.text_box.text
      
      from .... import form
      for target_id in self.tag.logic_target_ids:
        form.check_logic_for_visibility(target_id)

