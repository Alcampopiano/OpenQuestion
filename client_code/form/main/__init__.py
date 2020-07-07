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
    Notification('You may close this window', 
                 title='Your data have been submitted').show()
    
    
  def form_show(self, **event_args):
    
    for section in self.column_panel.get_components():
        self.color_rows(section)
        
    self.column_panel.get_components()[0].section_select()
    
    
  def color_rows(self, section, **event_args):
          
    for i, comp in enumerate(section.column_panel.get_components()):
  
      if not i%2:
        comp.background='theme:Gray 100'
        
      else:
        comp.background='white'
    
