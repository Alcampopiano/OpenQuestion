import anvil.server
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .confirm_content import confirm_content

def show_branch_ui(current_widget):
  
  titles=[]
  widgets=[]
  for section in get_open_form().column_panel.get_components():
    
    for widget in section.column_panel.get_components():
      
      if widget.__name__ not in ('markdown', 'text_area', 'check_box') and\
        widget != current_widget:
        
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
    #logic_target_ids=[flow.tag.logic_target_id for flow in content.column_panel.get_components()]
    
    if conditions:
     
      logic={'func': 'any' if content.radio_button_any.selected else 'all'}
      logic['conditions']=conditions
      current_widget.tag.logic=logic
      current_widget.tag.visible=False
      
    else:
      current_widget.tag.visible=True
      current_widget.tag.logic=None
      
  
      
