import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import *
from .. import widgets

def build_form(schema, column_panel):
  
  column_panel.tag.title=schema['title']
  column_panel.tag.id=schema['id']
  print(schema)
  
  for section_schema in schema['widgets']:
    
    section=widgets.section()
    section.text_box_title.text=section_schema['title']
    section.tag.id=section_schema
    section.tag.logic=section_schema['logic']
    
    for widget_schema in section_schema['widgets']:
      
      if widget_schema['type']=='text_box':
        
        widget=widgets.text_box(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.text_box.text=widget_schema['text']
        
#       elif widget_schema['type']=='drop_down':
#         pass
        
#       elif widget_schema['type']=='date':
#         pass
      
        widget.tag.logic=widget_schema['logic']
        widget.tag.id=widget_schema['id']
        section.column_panel.add_component(widget)
    
    column_panel.add_component(section)
    
    
    
    
    
def build_schema(column_panel):
  pass
 

