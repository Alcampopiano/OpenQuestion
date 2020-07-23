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

    # Any code you write here will run when the form opens.
    from ..toolbar import toolbar
    toolbar=toolbar(align='left', section=section, parent=self)
    
    self.add_component(toolbar)

  def render_click(self, **event_args):
    """This method is called when the button is clicked"""
    text=self.text_area_text.text
    html=anvil.server.call('convert_markdown',text)
    self.html_display.html=html
    self.column_panel_container.visible=True

