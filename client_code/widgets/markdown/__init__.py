from ._anvil_designer import markdownTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class markdown(markdownTemplate):
  def __init__(self, section, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
        
    from ..toolbar import toolbar
    toolbar=toolbar(align='left', section=section, parent=self)
    self.add_component(toolbar)

#     # Any code you write here will run when the form opens.
#   def button_1_click(self, **event_args):
#     self.html_display_1.html = \
#       anvil.server.call('convert_markdown', 
#                           self.text_area_markdown.text)
