from ._anvil_designer import sectionTemplate
from anvil import *

class section(sectionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
             
  def form_show(self, **event_args):
    self.border='solid red .5px'
    get_open_form().tag.active_section=self
    self.section_border_toggle()
    from ..toolbar import toolbar

    toolbar=toolbar()
    self.column_panel.add_component(toolbar)
  
  def section_border_toggle(self, **event_args):
    
      sections=get_open_form().content_panel.get_components()
  
      for section in sections:
        if section is not self:
          section.border='solid gray .5px'
          
  def section_select(self, **event_args):
    
    if self.border is 'solid gray .5px':
      self.border='solid red .5px'
      get_open_form().tag.active_section=self
      self.section_border_toggle()
    
      
      
      
    

