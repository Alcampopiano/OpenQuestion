import anvil.server
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from . import widgets
from .widgets.widget_utilities.hr import hr

def submit_data(column_panel):
  
  df_dict={}
  cols=[]
  data=[]
  
  for section in column_panel.get_components():
    
    
    for widget in section.column_panel.get_components():
                  
      if 'text_box' is widget.__name__:
        
        col=widget.label_title.text
        val=widget.text_box.text
        
        if widget.label_mandatory.visible and not val.strip():
          alert('Responses have not been submitted', title="Please fill out the mandatory fields")
          return
    
      elif 'drop_down' is widget.__name__:
        
        col=widget.label_title.text
        val=widget.drop_down.selected_value
        
        if widget.label_mandatory.visible and not val:
          alert('Responses have not been submitted', title="Please fill out the mandatory fields")
          return
     
      elif 'date' is widget.__name__:
        
        col=widget.label_title.text
        val=widget.date_picker.date
        
        if widget.label_mandatory.visible and not val:
          alert('Responses have not been submitted', title="Please fill out the mandatory fields")
          return
        
      elif 'check_box' is widget.__name__:
        
        col=widget.label_title.text
        
        val=[]
        for c in widget.column_panel.get_components():
          if c.checked:
            val.append(c.text)
            
        val='' if not val else val
        
      elif 'radio_button' is widget.__name__:
        
        col=widget.label_title.text
        
        for c in widget.column_panel.get_components():
          if c.selected:
            val=c.text
            break
        
      elif 'text_area' is widget.__name__:
        
        col=widget.label_title.text
        val=widget.text_area.text
        
      elif 'slider' is widget.__name__:
        
        col=widget.label_title.text
        val=widget.label_value.text
        
      else:
        continue
    
      cols.append(col)
      data.append(val)
      
  anvil.server.call('submit_data', cols, data, get_url_hash())
  Notification('You may close this window', 
                 title='Your data have been submitted').show()
      
    

def build_form(schema, column_panel):
  
  main=column_panel.parent
  main.tag.form_dict={}
  
  for section_schema in schema['widgets']:
    
    section=widgets.section()
    section.label_title.text=section_schema['title']
    section.tag.logic=section_schema['logic']
    section.tag.id=section_schema['id']
    section.visible=False if section_schema['logic'] else True
    
    for widget_schema in section_schema['widgets']:
      
      if widget_schema['type']=='text_box':
        
        widget=widgets.text_box()
        widget.label_title.text=widget_schema['title']
        widget.text_box.placeholder=widget_schema['placeholder']
        widget.label_mandatory.visible=widget_schema['mandatory']
        
      elif widget_schema['type']=='drop_down':
        widget=widgets.drop_down()
        widget.label_title.text=widget_schema['title']
        widget.drop_down.items=widget_schema['options'].split('\n')
        widget.drop_down.placeholder=widget_schema['placeholder']
        widget.label_mandatory.visible=widget_schema['mandatory']

      elif widget_schema['type']=='date':
        widget=widgets.date()
        widget.label_title.text=widget_schema['title']
        widget.date_picker.format=widget_schema['format']
        widget.date_picker.placeholder=widget_schema['placeholder']
        widget.label_mandatory.visible=widget_schema['mandatory']
        
      elif widget_schema['type']=='check_box':
        options=widget_schema['options'].split('\n')
        widget=widgets.check_box(options=options)
        widget.label_title.text=widget_schema['title']
      
      elif widget_schema['type']=='radio_button':
        options=widget_schema['options'].split('\n')
        widget=widgets.radio_button(options=options)
        widget.label_title.text=widget_schema['title']
        
      elif widget_schema['type']=='markdown':
        widget=widgets.markdown()
        html = anvil.server.call_s('convert_markdown', widget_schema['text'])
        widget.html_display.html=html
        
      elif widget_schema['type']=='text_area':
        
        widget=widgets.text_area()
        widget.label_title.text=widget_schema['title']
        widget.text_area.placeholder=widget_schema['placeholder']
        
      elif widget_schema['type']=='slider':
        
        widget=widgets.slider()
        widget.label_value.text=widget_schema['value']
        widget.label_title.text=widget_schema['title']
        widget.slider.labels=widget_schema['labels'].split('\n')
        widget.slider.min_val=widget_schema['min_val']
        widget.slider.max_val=widget_schema['max_val']
        widget.slider.value=widget_schema['value']
        widget.slider.step=widget_schema['step']
        
      widget.tag.logic=widget_schema['logic']
      widget.visible=False if widget_schema['logic'] else True
      widget.tag.id=widget_schema['id']
      section.column_panel.add_component(widget)
      
      # save to flat structure on main form
      main.tag.form_dict[widget_schema['id']]=widget
    
    column_panel.add_component(section)
    
    # save to flat structure on main form
    main.tag.form_dict[section_schema['id']]=section
    
  set_logic_target_ids(main.tag.form_dict)

def set_logic_target_ids(form_dict):
    
  target_logic_components=[form_dict[k] for k in form_dict if form_dict[k].tag.logic]

  for target_comp in target_logic_components:
    for source_dict in target_comp.tag.logic['conditions']:
      form_dict[source_dict['id']].tag.logic_target_ids.append(target_comp.tag.id)

      
def check_logic_for_visibility(target_id):
  
      form_dict=get_open_form().tag.form_dict
      logic=form_dict[target_id].tag.logic
          
      truth_array=[]
      for condition in logic['conditions']:
        
        source_comp=form_dict[condition['id']]
        comparison=condition['comparison']
        actual_val=source_comp.tag.current_value  
        
        # escape doing nothing if actual value is None
        if not actual_val:
          return
        
        if source_comp.__name__=='date':
          test_val=anvil.server.call_s('str_to_date_obj', 
                                          condition['value'], 
                                          source_comp.date_picker.format)
        else:
          test_val=condition['value']
        
        if comparison=='>':
          truth_array.append(actual_val>test_val)
          
        elif comparison=='<':
          truth_array.append(actual_val<test_val)
          
        elif comparison=='=':
          truth_array.append(actual_val==test_val)
          
        elif comparison=='!=':
          truth_array.append(actual_val!=test_val)
          
        elif comparison=='<=':
          truth_array.append(actual_val<=test_val) 
          
        elif comparison=='>=':
          truth_array.append(actual_val>=test_val)
      
#         print('comparison', condition['comparison'])
#         print('test_val', test_val)
#         print('actual_val', actual_val)
      
#       print('truth array', truth_array)
#       print('func', logic['func'])
      
      if logic['func'] == 'any' and any(truth_array):
        form_dict[target_id].visible=True
        
      elif logic['func'] == 'all' and truth_array and all(truth_array):
        form_dict[target_id].visible=True

      else:
        form_dict[target_id].visible=False
        
      get_open_form().hide_last_hr()
      