from ._anvil_designer import text_boxTemplate
from anvil import *

class text_box(text_boxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

