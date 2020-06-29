from ._anvil_designer import toolbarTemplate
from anvil import *

class toolbar(toolbarTemplate):
  
  def __init__(self, align, section, parent, **properties):

    self.init_components(**properties)
    
    self.tag.parent=parent
    self.tag.is_section=section == parent
    self.tag.section=section
    self.tag.parent=parent
    
    if align=='center':
      self.flow_panel.align='center'
   
  def remove_parent(self, **event_args):
    self.tag.parent.remove_from_parent()
    
    if not self.tag.is_section:
      get_open_form().color_rows()
      
  def move_up(self, **event_args):
    
    if not self.tag.is_section:
      print(len(self.tag.section.column_panel.get_components()))
   

