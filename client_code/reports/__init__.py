import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
from . import widgets

def build_report(schema, charts_dict, column_panel):
  
  column_panel.tag.title=schema['title']
  main=column_panel.parent
  main.tag.form_dict={}
  #column_panel.tag.id=schema['id']
  
  for section_schema in schema['widgets']:
    
    section=widgets.section()
    section.text_box_title.text=section_schema['title']
    section.label_id.text=section_schema['id']
    
    for widget_schema in section_schema['widgets']:
      
      if widget_schema['type']=='chart':
        
        widget=widgets.chart(section=section)
        widget.tag.chart.tag.vl_spec=charts_dict[str(widget_schema['id'])]
        
      elif widget_schema['type']=='markdown':
        widget=widgets.markdown(section=section)
        widget.text_area_text.text=widget_schema['text']
        
      widget.label_id.text=widget_schema['id']
          
      # save to flat structure on main form
      main.tag.form_dict[widget_schema['id']]=widget
    
      section.column_panel.add_component(widget)
        
    # save to flat structure on main form
    main.tag.form_dict[section_schema['id']]=section
    
    column_panel.add_component(section)

    
def build_schema(column_panel):
  
  schema={}
  chart_dict={}
  schema['title']=get_open_form().text_box_title.text 
  #schema['id']=get_open_form().tag.id # column_panel.tag.id
  schema['num_widgets']=get_open_form().tag.num_widgets
  schema['widgets']=[]

  for section in column_panel.get_components():
  
    section_schema={}
    section_schema['type']='section'
    section_schema['title']=section.text_box_title.text
    section_schema['id']=section.label_id.text
    section_schema['widgets']=[]
    
    for widget in section.column_panel.get_components():
      
      widget_schema={}
      widget_schema['id']=widget.label_id.text
      
      if 'chart' is widget.__name__:
        
        widget_schema['type']='chart'
        chart_dict[str(widget_schema['id'])]=widget.tag.chart.tag.vl_spec
    
      elif 'markdown' is widget.__name__:
        
        widget_schema['type']='markdown'
        widget_schema['text']=widget.text_area_text.text
    
      section_schema['widgets'].append(widget_schema)
      
    schema['widgets'].append(section_schema)
    
  print(schema, chart_dict)
  return schema, chart_dict

    

  

 

