from ._anvil_designer import confirm_contentTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class confirm_content(confirm_contentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.tag.background='white'

  def add_click(self, **event_args):
    
    items=self.flow_panel_build_condition.get_components()
    
    show_label=Label(text=items[0].selected_value)
    if_label=Label(text='if', align='center')
    widget_label=Label(
      text=f"{items[2].selected_value.text_box_title.text} (id: {items[2].selected_value.label_id.text})")
    
    oper_label=Label(text=items[3].selected_value)
    
    if str(type(items[4])) is "<class 'anvil.TextBox'>":
      val_text=items[4].text 
    else:
      val_text=items[4].selected_value
      
    val_label=Label(text=val_text)
    minus_but=Button(text='remove', icon='fa:minus-circle')
    minus_but.set_event_handler('click', self.minus_click)
    
    if self.tag.background=='white':
      background='theme:Gray 200'
      self.tag.background=background
    else:
      background='white' 
      self.tag.background=background
      
    cond_flow=FlowPanel(background=background, spacing_above=None, spacing_below=None)
    cond_flow.add_component(show_label)   
    cond_flow.add_component(widget_label)
    cond_flow.add_component(if_label)
    cond_flow.add_component(oper_label)
    cond_flow.add_component(val_label)
    cond_flow.add_component(minus_but)
    self.column_panel.add_component(cond_flow)
    
  def minus_click(self, **event_args):
    parent=event_args['sender'].parent
    parent.remove_from_parent()
    
  def widget_change(self, **event_args):
    """This method is called when an item is selected"""
    
    if len(self.flow_panel_build_condition.get_components())>4:
      self.flow_panel_build_condition.get_components()[-1].remove_from_parent()
    
    if self.drop_down_widgets.selected_value.__name__ in \
      ('drop_down', 'radio_button'):
      
      items=self.drop_down_widgets.selected_value.text_area_options.text.split('\n')
      val_comp=DropDown(items=items)
      self.flow_panel_build_condition.add_component(val_comp)
      
    elif self.drop_down_widgets.selected_value.__name__ == 'date':
      val_comp=DatePicker(placeholder='choose a date')
      self.flow_panel_build_condition.add_component(val_comp)
      
    else:
      val_comp=TextBox(type='number', placeholder='type number')
      self.flow_panel_build_condition.add_component(val_comp)

      
      


