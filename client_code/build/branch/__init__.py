import anvil.server
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .confirm_content import confirm_content

def show_branch_ui(current_widget):
  
  form_dict=get_open_form().tag.form_dict
  titles=[]
  widgets=[]
  
  for k in form_dict:
    
    widget=form_dict[k]

    if widget.__name__ is 'text_box' and widget.check_box_number.checked==False:
      continue

    if widget.__name__ not in ('section', 'markdown', 'text_area', 'check_box')\
      and widget != current_widget:
      
      titles.append(widget.text_box_title.text + f" (id: {widget.label_id.text})")
      widgets.append(widget)
          
  drop_tuples=list(zip(titles, widgets))
  content=confirm_content(current_widget)
  content.drop_down_widgets.items=drop_tuples
  
  current_label=f'markdown widget (id: {current_widget.label_id.text})' \
    if 'markdown' in str(type(current_widget)) \
    else f'{current_widget.text_box_title.text} (id: {current_widget.label_id.text})'
  
  c=confirm(content, title=current_label, large=True, 
            buttons=[('apply', 'apply'), ('cancel', 'cancel')])
  
  if c == 'apply':
    
    conditions=[flow.tag.logic for flow in content.column_panel.get_components()]
          
    if conditions:
      
      for condition in conditions:
        source_comp=get_open_form().tag.form_dict[condition['id']]
        print(source_comp.text_box_title.text)
        source_comp.tag.logic_target_ids.append(current_widget.label_id.text)
     
      logic={'func': 'any' if content.radio_button_any.selected else 'all'}
      logic['conditions']=conditions
      current_widget.tag.logic=logic
      current_widget.tag.visible=False
      
    else:
      current_widget.tag.visible=True
      current_widget.tag.logic=None
      
  
      
