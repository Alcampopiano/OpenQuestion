import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import *
from . import widgets

def build_form(schema, column_panel):
  
  column_panel.tag.title=schema['title']
  main=column_panel.parent
  main.tag.form_dict={}
  #column_panel.tag.id=schema['id']
  
  for section_schema in schema['widgets']:
    
    section=widgets.section()
    section.text_box_title.text=section_schema['title']
    section.tag.logic=section_schema['logic']
    #section.visible=section_schema['visible']
    section.label_id.text=section_schema['id']
    
    for widget_schema in section_schema['widgets']:
      
      if widget_schema['type']=='text_box':
        
        widget=widgets.text_box(section=section)
        widget.text_box_placeholder.text=widget_schema['placeholder']
        widget.check_box_mandatory.checked=widget_schema['mandatory']
        
      elif widget_schema['type']=='drop_down':
        widget=widgets.drop_down(section=section)
        widget.text_area_options.text=widget_schema['options']
        widget.text_box_placeholder.text=widget_schema['placeholder']
        widget.check_box_mandatory.checked=widget_schema['mandatory']
        
      elif widget_schema['type']=='date':
        widget=widgets.date(section=section)
        widget.text_box_format.text=widget_schema['format']
        widget.text_box_placeholder.text=widget_schema['placeholder']
        widget.check_box_mandatory.checked=widget_schema['mandatory']
        
      elif widget_schema['type']=='check_box':
        widget=widgets.check_box(section=section)
        widget.text_area_options.text=widget_schema['options']
        
      elif widget_schema['type']=='radio_button':
        widget=widgets.radio_button(section=section)
        widget.text_area_options.text=widget_schema['options']
        
      elif widget_schema['type']=='markdown':
        widget=widgets.markdown(section=section)
        widget.text_area_text.text=widget_schema['text']
        widget.text_area_text.placeholder=widget_schema['placeholder']
        
      elif widget_schema['type']=='text_area':
        widget=widgets.text_area(section=section)
        widget.text_box_placeholder.text=widget_schema['placeholder']
        
      elif widget_schema['type']=='slider':
        widget=widgets.slider(section=section)
        widget.text_box_min_val.text=widget_schema['min_val']
        widget.text_box_max_val.text=widget_schema['max_val']
        widget.text_box_step.text=widget_schema['step']
        widget.text_box_value.text=widget_schema['value']
        widget.text_area_labels.text=widget_schema['labels']
        
      widget.text_box_title.text=widget_schema['title']
      widget.label_id.text=widget_schema['id']
      widget.tag.logic=widget_schema['logic']
      #widget.visible=widget_schema['visible']
          
      # save to flat structure on main form
      main.tag.form_dict[widget_schema['id']]=widget
    
      section.column_panel.add_component(widget)
        
    # save to flat structure on main form
    main.tag.form_dict[section_schema['id']]=section
    
    column_panel.add_component(section)
    
  # set logic target ids
  #set_target_ids(main.tag.form_dict)

    
def build_schema(column_panel):
  
  schema={}
  schema['title']=get_open_form().text_box_title.text 
  #schema['id']=get_open_form().tag.id # column_panel.tag.id
  schema['num_widgets']=get_open_form().tag.num_widgets
  schema['widgets']=[]

  for section in column_panel.get_components():
  
    section_schema={}
    section_schema['type']='section'
    section_schema['title']=section.text_box_title.text
    section_schema['id']=section.label_id.text
    #section_schema['visible']=True#section.tag.visible
    section_schema['logic']=section.tag.logic
    section_schema['widgets']=[]
    
    for widget in section.column_panel.get_components():
      
      widget_schema={}
      #widget_schema['visible']=True#widget.tag.visible
      widget_schema['logic']=widget.tag.logic
      #print(widget.tag.logic)
      widget_schema['id']=widget.label_id.text
      widget_schema['title']=widget.text_box_title.text
      
      if 'text_box' is widget.__name__:
        
        widget_schema['type']='text_box'
        widget_schema['placeholder']=widget.text_box_placeholder.text
        widget_schema['mandatory']=widget.check_box_mandatory.checked
        widget_schema['number']=widget.check_box_number.checked
    
      elif 'drop_down' is widget.__name__:
        
        widget_schema['type']='drop_down'
        widget_schema['placeholder']=widget.text_box_placeholder.text
        widget_schema['options']=widget.text_area_options.text
        widget_schema['mandatory']=widget.check_box_mandatory.checked
     
      elif 'date' is widget.__name__:
        
        widget_schema['type']='date'
        widget_schema['placeholder']=widget.text_box_placeholder.text
        widget_schema['format']=widget.text_box_format.text
        widget_schema['mandatory']=widget.check_box_mandatory.checked
        
      elif 'check_box' is widget.__name__:
        
        widget_schema['type']='check_box'
        widget_schema['options']=widget.text_area_options.text
        
      elif 'radio_button' is widget.__name__:
        
        widget_schema['type']='radio_button'
        widget_schema['options']=widget.text_area_options.text
        
      elif 'markdown' is widget.__name__:
        
        widget_schema['type']='markdown'
        widget_schema['placeholder']=widget.text_area_text.placeholder
        widget_schema['text']=widget.text_area_text.text
        
      elif 'text_area' is widget.__name__:
        
        widget_schema['type']='text_area'
        widget_schema['placeholder']=widget.text_box_placeholder.text
        
      elif 'slider' is widget.__name__:
        
        widget_schema['type']='slider'
        widget_schema['min_val']=widget.text_box_min_val.text
        widget_schema['max_val']=widget.text_box_max_val.text
        widget_schema['step']=widget.text_box_step.text
        widget_schema['value']=widget.text_box_value.text
        widget_schema['labels']=widget.text_area_labels.text
    
      section_schema['widgets'].append(widget_schema)
      
    schema['widgets'].append(section_schema)
    
  return schema

    

  

 

