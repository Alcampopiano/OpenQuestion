from ._anvil_designer import markdownTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ....utilities import augment


class markdown(markdownTemplate):
  def __init__(self, section, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.tag.logic=None
    #self.tag.visible=True
        
    from ..toolbar import toolbar
    toolbar=toolbar(align='left', section=section, parent=self)
    self.add_component(toolbar)
    
    augment.set_event_handler(self.column_panel_outer, 'click', 
                              self.column_panel_outer_click)

  def text_area_lost_focus(self, **event_args):
    
    text=self.text_area_text.text
    
    if text:
      html=anvil.server.call('convert_markdown',text)
      self.markdown_display.html=html
      self.column_panel_outer.visible=True
      self.text_area_text.visible=False
    
  def column_panel_outer_click(self, **event_args):
    self.text_area_text.visible=True
    self.column_panel_outer.visible=False


