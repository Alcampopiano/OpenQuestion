import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import *
from .. import widgets

'%d %b, %Y %H:%M:%S'

def build_form(schema, column_panel):
  
  column_panel.tag.title=schema['title']
  #column_panel.tag.id=schema['id']
  
  for section_schema in schema['widgets']:
    
    section=widgets.section()
    section.text_box_title.text=section_schema['title']
    #section.tag.id=section_schema['id']
    #section.tag.logic=section_schema['logic']
    section.label_id.text=section_schema['id']
    
    for widget_schema in section_schema['widgets']:
      
      if widget_schema['type']=='text_box':
        
        widget=widgets.text_box(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.text_box_placeholder.placeholder=widget_schema['placeholder']
        widget.label_id.text=widget_schema['id']
        widget.check_box_mandatory.checked=widget_schema['mandatory']
        
      elif widget_schema['type']=='drop_down':
        widget=widgets.drop_down(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.text_area_options.text=widget_schema['options']
        widget.text_box_placeholder.placeholder=widget_schema['placeholder']
        widget.label_id.text=widget_schema['id']
        widget.check_box_mandatory.checked=widget_schema['mandatory']
        
      elif widget_schema['type']=='date':
        widget=widgets.date(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.text_box_format.text=widget_schema['format']
        widget.text_box_placeholder.placeholder=widget_schema['placeholder']
        widget.label_id.text=widget_schema['id']
        widget.check_box_mandatory.checked=widget_schema['mandatory']
        
      elif widget_schema['type']=='check_box':
        widget=widgets.check_box(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.text_area_options.text=widget_schema['options']
        widget.label_id.text=widget_schema['id']
        
      elif widget_schema['type']=='radio_button':
        widget=widgets.radio_button(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.text_area_options.text=widget_schema['options']
        widget.label_id.text=widget_schema['id']
        
      elif widget_schema['type']=='markdown':
        widget=widgets.markdown(section=section)
        widget.text_area_text.text=widget_schema['text']
        widget.text_area_text.placeholder=widget_schema['placeholder']
        widget.label_id.text=widget_schema['id']
        
      elif widget_schema['type']=='text_area':
        widget=widgets.text_area(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.text_box_placeholder.text=widget_schema['placeholder']
        widget.label_id.text=widget_schema['id']
        
      elif widget_schema['type']=='slider':
        widget=widgets.slider(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.label_id.text=widget_schema['id']
        widget.text_box_min_val.text=widget_schema['min_val']
        widget.text_box_max_val.text=widget_schema['max_val']
        widget.text_box_step.text=widget_schema['step']
        widget.text_box_value.text=widget_schema['value']
        widget.text_area_labels.text=widget_schema['labels']

      # remove this once all components are accounted for
      if widget_schema['type'] in ('text_box', 'drop_down', 'date', 
                                   'check_box', 'radio_button', 'markdown', 
                                   'text_area', 'slider'):
        
        widget.tag.logic=widget_schema['logic']
        #widget.tag.id=widget_schema['id']
        section.column_panel.add_component(widget)

    
    column_panel.add_component(section)
    
    
def build_schema(column_panel):
  
  schema={}
  schema['title']=get_open_form().text_box_title.text #column_panel.text_box_title.text
  #schema['id']=get_open_form().tag.id # column_panel.tag.id
  schema['num_widgets']=get_open_form().tag.num_widgets
  schema['widgets']=[]

  for section in column_panel.get_components():
  
    section_schema={}
    section_schema['type']='section'
    section_schema['title']=section.text_box_title.text
    section_schema['id']=section.label_id.text
    section_schema['visible']=True # should be a tag property
    section_schema['logic']=None # should be a tag property
    section_schema['widgets']=[]
    
    for widget in section.column_panel.get_components():
      
      widget_schema={}
      
      if 'text_box' in str(type(widget)):
        
        widget_schema['type']='text_box'
        widget_schema['title']=widget.text_box_title.text
        widget_schema['id']=widget.label_id.text
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        widget_schema['placeholder']=widget.text_box_placeholder.text
        widget_schema['mandatory']=widget.check_box_mandatory.checked
    
      elif 'drop_down' in str(type(widget)):
        
        widget_schema['type']='drop_down'
        widget_schema['title']=widget.text_box_title.text
        widget_schema['id']=widget.label_id.text
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        widget_schema['placeholder']=widget.text_box_placeholder.text
        widget_schema['options']=widget.text_area_options.text
        widget_schema['mandatory']=widget.check_box_mandatory.checked
     
      elif 'date' in str(type(widget)):
        
        widget_schema['type']='date'
        widget_schema['title']=widget.text_box_title.text
        widget_schema['id']=widget.label_id.text
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        widget_schema['placeholder']=widget.text_box_placeholder.text
        widget_schema['format']=widget.text_box_format.text
        widget_schema['mandatory']=widget.check_box_mandatory.checked
        
      elif 'check_box' in str(type(widget)):
        
        widget_schema['type']='check_box'
        widget_schema['title']=widget.text_box_title.text
        widget_schema['id']=widget.label_id.text
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        widget_schema['options']=widget.text_area_options.text
        
      elif 'radio_button' in str(type(widget)):
        
        widget_schema['type']='radio_button'
        widget_schema['title']=widget.text_box_title.text
        widget_schema['id']=widget.label_id.text
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        widget_schema['options']=widget.text_area_options.text
        
      elif 'markdown' in str(type(widget)):
        
        widget_schema['type']='markdown'
        widget_schema['placeholder']=widget.text_area_text.placeholder
        widget_schema['text']=widget.text_area_text.text
        widget_schema['id']=widget.label_id.text
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        
      elif 'text_area' in str(type(widget)):
        
        widget_schema['type']='text_area'
        widget_schema['title']=widget.text_box_title.text
        widget_schema['id']=widget.label_id.text
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        widget_schema['placeholder']=widget.text_box_placeholder.text
        
      elif 'slider' in str(type(widget)):
        
        widget_schema['type']='slider'
        widget_schema['title']=widget.text_box_title.text
        widget_schema['id']=widget.label_id.text
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        widget_schema['min_val']=widget.text_box_min_val.text
        widget_schema['max_val']=widget.text_box_max_val.text
        widget_schema['step']=widget.text_box_step.text
        widget_schema['value']=widget.text_box_value.text
        widget_schema['labels']=widget.text_area_labels.text
    
    
      section_schema['widgets'].append(widget_schema)
      
    schema['widgets'].append(section_schema)
    
  return schema
 

