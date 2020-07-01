from ._anvil_designer import select_formTemplate
from anvil import *

class select_form(select_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
