from ._anvil_designer import confirm_contentTemplate
from anvil import *
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class confirm_content(confirm_contentTemplate):
  
  def __init__(self, current_widget, **properties):

    self.init_components(**properties)
    
    if current_widget.tag.logic:
      
      logic=current_widget.tag.logic
      
      func=logic['func']
      
      if func=='all':
        self.radio_button_all.selected=True
        
      form_dict=get_open_form().tag.form_dict
      
      for d in logic['conditions']:
        show_label=Label(text='Show if')
        widget_label=Label(text=f"{form_dict[d['id']].text_box_title.text}  id: {d['id']}")
        oper_label=Label(text=d['comparison'])
        value_label=Label(text=d['value'])
        cond_flow=FlowPanel(background="theme:Gray 100", 
                          spacing_above=None, 
                          spacing_below=None)
        
        cond_flow.add_component(show_label)   
        cond_flow.add_component(widget_label)
        cond_flow.add_component(oper_label)
        cond_flow.add_component(value_label)
        
        minus_but=Button(text='remove', icon='fa:minus-circle')
        minus_but.set_event_handler('click', self.minus_click)
        cond_flow.add_component(minus_but)
        self.column_panel.add_component(cond_flow)
        
        cond_flow.tag.logic={
        'id': d['id'],
        'title': form_dict[d['id']].text_box_title.text,
        'comparison': d['comparison'],
        'value': d['value']}
    

  def add_click(self, **event_args):
    
    items=self.flow_panel_build_condition.get_components()
    widget=items[1].selected_value
    comparison=items[2]
    val=items[3]
    
    show_label=Label(text="Show if")
    widget_label=Label(italic=True,
      text=f"{widget.text_box_title.text} (id: {widget.label_id.text})")
    
    comparison_label=Label(text=comparison.selected_value)
    
    if type(val) is TextBox:
      val_text=val.text
      
    elif type(val) == DatePicker:
      val_text=str(val.date)
      
    else:
      val_text=val.selected_value
      
    val_label=Label(text=val_text)
    minus_but=Button(text='remove', icon='fa:minus-circle')
    minus_but.set_event_handler('click', self.minus_click)
      
    cond_flow=FlowPanel(background="theme:Gray 100", 
                        spacing_above=None, 
                        spacing_below=None)
    
    cond_flow.add_component(show_label)   
    cond_flow.add_component(widget_label)
    cond_flow.add_component(comparison_label)
    cond_flow.add_component(val_label)
    cond_flow.add_component(minus_but)
    self.column_panel.add_component(cond_flow)
    
    #print(val_label.text)
    #print(type(val_label.text))
    
    cond_flow.tag.logic={
      'id': widget.label_id.text,
      'title': widget.text_box_title.text,
      'comparison': comparison_label.text,
      'value': val_label.text} 
    
  def minus_click(self, **event_args):
    parent=event_args['sender'].parent
    parent.remove_from_parent()
    
  def widget_change(self, **event_args):
    
    if len(self.flow_panel_build_condition.get_components())>3:
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

      
      


