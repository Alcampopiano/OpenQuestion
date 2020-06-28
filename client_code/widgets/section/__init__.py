from ._anvil_designer import sectionTemplate
from anvil import *

class section(sectionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
             
  def form_show(self, **event_args):

    #self.border='solid red .5px'
    self.role='section_shadow'
    get_open_form().tag.active_section=self
    self.section_border_toggle()
    
    from ..toolbar import toolbar
    toolbar=toolbar(spacer_bool=False, center_widgets=True)
    self.link.add_component(toolbar)
  
  def section_border_toggle(self, **event_args):
    
      sections=get_open_form().content_panel.get_components()
  
      for section in sections:
        if section is not self:
          #section.border='solid gray .5px'
          section.role='section_no_shadow'
          
  def section_select(self, **event_args):
    
    if self.role=='section_no_shadow':
    #if self.border is 'solid gray .5px':
      #self.border='solid red .5px'
      self.role='section_shadow'
      get_open_form().tag.active_section=self
      self.section_border_toggle()
    
      
      
      
    

