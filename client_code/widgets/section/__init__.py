from ._anvil_designer import sectionTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...utilities import augment

class section(sectionTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)
    
    self.role='section_shadow'
    augment.set_event_handler(self, 'click', self.section_select)
    
    from ..toolbar import toolbar
    toolbar=toolbar(align='center', section=self, parent=self)
    #self.link.add_component(toolbar)
    self.add_component(toolbar)
      
  def form_show(self, **event_args):
    get_open_form().tag.active_section=self
    self.section_border_toggle()
    
  def section_border_toggle(self, **event_args):
    
      sections=get_open_form().column_panel.get_components()
  
      for section in sections:
        if section is not self:
          section.role='section_no_shadow'
          
  def section_select(self, **event_args):
    
    if self.role=='section_no_shadow':
      self.role='section_shadow'
      get_open_form().tag.active_section=self
      self.section_border_toggle()
    
      
      
      
    

