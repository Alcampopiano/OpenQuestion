from ._anvil_designer import sliderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class slider(sliderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # debouce to avoid form show firing twice for some reason
    self.tag.shown=False
    
    self.tag.logic=None
    self.tag.logic_target_ids=[]
    self.tag.current_value=None

  def form_show(self, **event_args):
    
    if not self.tag.shown:
      array=self.slider.labels
      min_val=self.slider.min_val
      max_val=self.slider.max_val
      step=self.slider.step
      value=self.slider.value
      self.call_js('set_tick_labels', self.slider, array, min_val, max_val, step, value)
      self.tag.shown=True      
    
  def slider_change(self, **event_args):
    self.label_value.text = self.slider.value
    self.tag.current_value=self.slider.value    