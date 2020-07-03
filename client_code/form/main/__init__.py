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

    self.label_title.text=schema['title']
    form.build_form(schema, self.column_panel)  
    
    
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
    
