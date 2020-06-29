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
        
      comp=self.tag.parent
      section=self.tag.section
      list_of_comps=section.column_panel.get_components()
      ind=list_of_comps.index(comp)
      
      if ind>0:
        list_of_comps.pop(ind) 
        list_of_comps.insert(ind-1, comp)
        section.column_panel.clear()
        [section.column_panel.add_component(item) for item in list_of_comps]
      
      
      

