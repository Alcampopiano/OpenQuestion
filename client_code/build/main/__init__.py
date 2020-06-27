from ._anvil_designer import mainTemplate
from anvil import *
from ... import widgets

class main(mainTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)
    
    save_button=Button(text='save', role='primary-color')
    save_button.set_event_handler('click', self.save_click)
    self.add_component(save_button)
        
  def save_click(self, **event_args):
    print('save')
    
  def section_widget_click(self, **event_args):
    section=widgets.section()
    self.content_panel.add_component(section)
    
  def text_box_widget_click(self, **event_args):
    comp=widgets.text_box()
    self.tag.active_section.column_panel.add_component(comp)
    

      
    






