import anvil.server
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .confirm_content import confirm_content

def show_branch_ui(parent):
  
  titles=[]
  ids=[]
  for section in get_open_form().column_panel.get_components():
    
    titles.append(section.text_box_title.text)
    ids.append(section.label_id.text)
    
    for widget in section.column_panel.get_components():
      
      if 'markdown' in str(type(widget)):
        titles.append('markdown_widget')
      else:
        titles.append(widget.text_box_title.text)
        
      ids.append(widget.label_id.text)
      
      
  content=confirm_content()
  content.repeating_panel_1.items=[{'titles': titles}]
  
  c=confirm(content, title="Create your logic", large=True, 
            buttons=[('apply', 'apply'), ('cancel', 'cancel')])
      
      
