import anvil.server
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import user_widgets

'https://RZCX3HWGWWPZJCOH.anvil.app/MLWEXSSLJT4I3SM3B4MURYXP#5bdbc005-055e-45ea-9a65-cd81529d59f5'

def submit_data(column_panel):
  
  df_dict={}
  cols=[]
  data=[]
  
  for section in column_panel.get_components():
    
    
    for widget in section.column_panel.get_components():
            
      if 'text_box' in str(type(widget)):
        
        col=widget.label_title.text
        val=widget.text_box.text
    
      elif 'drop_down' in str(type(widget)):
        
        col=widget.label_title.text
        val=widget.drop_down.selected_value
     
      elif 'date' in str(type(widget)):
        
        col=widget.label_title.text
        val=widget.date_picker.date
        
      elif 'check_box' in str(type(widget)):
        
        col=widget.label_title.text
        
        val=[]
        for c in widget.column_panel.get_components():
          if c.checked:
            val.append(c.text)
        
      elif 'radio_button' in str(type(widget)):
        
        col=widget.label_title.text
        
        for c in widget.column_panel.get_components():
          if c.selected:
            val=c.text
            break
        
      elif 'text_area' in str(type(widget)):
        
        col=widget.label_title.text
        val=widget.text_area.text
        
      else:
        continue
    
      cols.append(col)
      data.append(val)
      
  anvil.server.call('submit_data', cols, data, get_url_hash())
      
    

def build_form(schema, column_panel):
  
  #column_panel.tag.title=schema['title']
  #column_panel.tag.id=schema['id']
  
  for section_schema in schema['widgets']:
    
    section=user_widgets.section()
    section.label_title.text=section_schema['title']
    #section.tag.id=section_schema['id']
    #section.tag.logic=section_schema['logic']
    section.tag.id=section_schema['id']
    
    for widget_schema in section_schema['widgets']:
      
      if widget_schema['type']=='text_box':
        
        widget=user_widgets.text_box()
        widget.label_title.text=widget_schema['title']
        widget.text_box.placeholder=widget_schema['placeholder']
        #widget.tag.id=widget_schema['id']
        
      elif widget_schema['type']=='drop_down':
        widget=user_widgets.drop_down()
        widget.label_title.text=widget_schema['title']
        #widget.label_title.text=widget_schema['options'].replace('\n', '')
        widget.drop_down.items=widget_schema['options'].split('\n')
        widget.drop_down.placeholder=widget_schema['placeholder']
        #widget.tag.id=widget_schema['id']

      elif widget_schema['type']=='date':
        widget=user_widgets.date()
        widget.label_title.text=widget_schema['title']
        widget.date_picker.format=widget_schema['format']
        widget.date_picker.placeholder=widget_schema['placeholder']
        #widget.tag.id=widget_schema['id']
        
      elif widget_schema['type']=='check_box':
        options=widget_schema['options'].split('\n')
        widget=user_widgets.check_box(options=options)
        widget.label_title.text=widget_schema['title']
        #widget.tag.id=widget_schema['id']
      
      elif widget_schema['type']=='radio_button':
        options=widget_schema['options'].split('\n')
        widget=user_widgets.radio_button(options=options)
        widget.label_title.text=widget_schema['title']
        #widget.tag.id=widget_schema['id']
        
      elif widget_schema['type']=='markdown':
        widget=user_widgets.markdown()
        html = anvil.server.call_s('convert_markdown', widget_schema['text'])
        widget.html_display.html=html
        #widget.tag.id=widget_schema['id']
        
      elif widget_schema['type']=='text_area':
        
        widget=user_widgets.text_area()
        widget.label_title.text=widget_schema['title']
        widget.text_area.placeholder=widget_schema['placeholder']
        #widget.tag.id=widget_schema['id']

      # remove this once all components are accounted for
      if widget_schema['type'] in ('text_box', 'drop_down', 'date', 
                                   'check_box', 'radio_button',  'markdown', 'text_area'):
        
        widget.tag.logic=widget_schema['logic']
        widget.tag.id=widget_schema['id']
        section.column_panel.add_component(widget)

    
    column_panel.add_component(section)
