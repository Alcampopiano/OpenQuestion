from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import form

class main(mainTemplate):
  def __init__(self, schema, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    submit_button=Button(text='submit', role='primary-color')
    submit_button.set_event_handler('click', self.submit_click)
    self.add_component(submit_button)

    self.label_title.text=schema['title']
    form.build_form(schema, self.column_panel)  
    
  def submit_click(self, **event_args):
    form.submit_data(self.column_panel)
    
    
  def form_show(self, **event_args):
    #self.hide_last_hr()  
    self.color_rows()
    self.column_panel.get_components()[0].section_select()
    
    
  def color_rows(self, **event_args):
    
    for section in self.column_panel.get_components():
            
      for i, comp in enumerate(section.column_panel.get_components()):
  
        if not i%2:
          comp.background='theme:Gray 100'
          
        else:
          comp.background='white'
        
  def hide_last_hr(self, **event_args):
    
    for section in self.column_panel.get_components():
      
      found=False
      for comp in reversed(section.column_panel.get_components()):
        
        if comp.visible and not found:
          comp.hr.visible=False
          found=True
          
        else:
          comp.hr.visible=True
          
        
    
