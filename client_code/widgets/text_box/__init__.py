from ._anvil_designer import text_boxTemplate
from anvil import *

class text_box(text_boxTemplate):
  
  def __init__(self, section, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    from ..toolbar import toolbar
    toolbar=toolbar(align='left', section=section, parent=self)
    self.add_component(toolbar)

