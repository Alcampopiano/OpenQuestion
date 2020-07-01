from ._anvil_designer import toolbarTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class toolbar(toolbarTemplate):
  
  def __init__(self, align, section, parent, **properties):

    self.init_components(**properties)
    
    self.tag.parent=parent
    self.tag.is_section=section == parent
    self.tag.section=section
    self.tag.parent=parent
    self.link_down.tag.direction=1
    self.link_up.tag.direction=-1
    
    if align=='center':
      self.flow_panel.align='center'
   
  def remove_parent(self, **event_args):
    self.tag.parent.remove_from_parent()
    
    if not self.tag.is_section:
      get_open_form().color_rows()
      
  def move_widget(self, **event_args):
    
    direction=event_args['sender'].tag.direction
    section=self.tag.parent if not self.tag.is_section else get_open_form()
            
    comp=self.tag.parent 
    items=section.column_panel.get_components()
    ind=items.index(comp)
      
    if (ind>0 and direction==-1) or (ind<len(items)-1 and direction==1):
      items[ind+direction], items[ind] = items[ind], items[ind+direction]
      section.column_panel.clear()
      [section.column_panel.add_component(item) for item in items]
      
      
      
      

