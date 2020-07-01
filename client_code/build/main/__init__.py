from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import widgets
from ... import build

class main(mainTemplate):
  def __init__(self, row=None, **properties):

    self.init_components(**properties)
    
    self.tag.row=row
    save_button=Button(text='save', role='primary-color')
    save_button.set_event_handler('click', self.save_click)
    self.add_component(save_button)
    
    if row:
      build.build_form(row['schema'], self.column_panel)
      
  def save_click(self, **event_args):
    print('save')
    
  def form_show(self, **event_args):
    
    if not self.tag.row:
      self.section_widget_click()
      
    else:
      
      for section in self.column_panel.get_components():
        self.color_rows(section)
        
      section.section_select()
    
    
  def section_widget_click(self, **event_args):
    section=widgets.section()
    self.column_panel.add_component(section)
    
  def text_box_widget_click(self, **event_args):
    comp=widgets.text_box(section=self.tag.active_section)
    self.tag.active_section.column_panel.add_component(comp)
    self.color_rows(self.tag.active_section)
    
  def color_rows(self, section, **event_args):
            
    for i, comp in enumerate(section.column_panel.get_components()):

      if i%2:
        comp.background='theme:Gray 100'
        
      else:
        comp.background='white'
          
       
  def link_select_form_click(self, **event_args):
     open_form('build.select_form')







