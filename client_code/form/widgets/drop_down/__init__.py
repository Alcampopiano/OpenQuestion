from ._anvil_designer import drop_downTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class drop_down(drop_downTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.tag.logic=None
    self.tag.logic_target_ids=[]
    self.tag.current_value=None

  def drop_down_change(self, **event_args):
    self.tag.current_value=self.drop_down.selected_value

    from .... import form
    for target_id in self.tag.logic_target_ids:
      form.check_logic_for_visibility(target_id)
      

        

