from ._anvil_designer import toolbarTemplate
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
from ... import branch

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
    
    del get_open_form().tag.form_dict[self.tag.parent.label_id.text]
    self.tag.parent.remove_from_parent()
    
    if not self.tag.is_section:
      get_open_form().color_rows(self.tag.section)
      
  def move_widget(self, **event_args):
    
    direction=event_args['sender'].tag.direction
    section=self.tag.section if not self.tag.is_section else get_open_form()
    comp=self.tag.parent 
    items=section.column_panel.get_components()
    ind=items.index(comp)
      
    if (ind>0 and direction==-1) or (ind<len(items)-1 and direction==1):
      items[ind+direction], items[ind] = items[ind], items[ind+direction]
      section.column_panel.clear()
      [section.column_panel.add_component(item) for item in items]
      
    if not self.tag.is_section:
      get_open_form().color_rows(self.tag.section)
      

  def click_branch(self, **event_args):
    
    branch.show_branch_ui(self.tag.parent)
    self.form_show()

  def form_show(self, **event_args):
    
    if self.tag.parent.tag.logic:
      self.link_branch.foreground='theme:Secondary 700'
    else:
      self.link_branch.foreground='theme:Primary 700'



