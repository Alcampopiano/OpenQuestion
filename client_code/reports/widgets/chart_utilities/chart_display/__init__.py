from ._anvil_designer import chart_displayTemplate
from anvil import *

class chart_display(chart_displayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self._vl_spec = {}
    self._shown = False
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  @property
  def vl_spec(self):
    return self._vl_spec
  
  @vl_spec.setter
  def vl_spec(self, new_val):
    self._vl_spec = new_val
    if self._shown:
      self.call_js('initVegaLite', self._vl_spec)
    
  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    self._shown = True
    # Fire the setter again to call the init function
    self.vl_spec = self._vl_spec