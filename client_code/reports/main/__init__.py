from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from ... import charts
from .. import widgets

class main(mainTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)
    
    #self.tag.row=row
    self.tag.form_dict={}
    self.tag.num_widgets=0
    save_button=Button(text='save', role='primary-color')
    save_button.set_event_handler('click', self.save_click)
    self.add_component(save_button)

      
  def save_click(self, **event_args):
    #schema=build.build_schema(self.column_panel)
    #form_id=anvil.server.call('save_schema', self.tag.id, schema)
    #self.tag.id=form_id
    #self.share_link_click.url=anvil.server.get_app_origin() + '#' + form_id
    pass

  def form_show(self, **event_args):
    self.section_widget_click()
      
    
    
  def color_rows(self, section, **event_args):
            
    for i, comp in enumerate(section.column_panel.get_components()):

      if not i%2:
        comp.background='theme:Gray 100'
        
      else:
        comp.background='white'
          
  def link_landing_click(self, **event_args):
     open_form('landing.select_action')

  def share_link_click(self, **event_args):
    
    if not self.share_link_click.url:
      Notification('',title='Please save the form first').show()

    else:
      #schema=build.build_schema(self.column_panel)
      #anvil.server.call('save_schema', self.tag.id, schema)
      pass
    
  def markdown_widget_click(self, **event_args):
    """This method is called when the link is clicked"""
    comp=widgets.markdown(section=self.tag.active_section)
    self.tag.active_section.column_panel.add_component(comp)
    self.color_rows(self.tag.active_section)
    comp.label_id.text=self.tag.num_widgets
    self.tag.num_widgets+=1
    self.tag.form_dict[comp.label_id.text]=comp
    
  def section_widget_click(self, **event_args):
    section=widgets.section()
    self.column_panel.add_component(section)
    section.label_id.text=self.tag.num_widgets
    self.tag.num_widgets+=1
    self.tag.form_dict[section.label_id.text]=section

  def chart_widget_click(self, **event_args):
    comp=widgets.chart(section=self.tag.active_section)
    self.tag.active_section.column_panel.add_component(comp)
    self.color_rows(self.tag.active_section)
    comp.label_id.text=self.tag.num_widgets
    self.tag.num_widgets+=1
    self.tag.form_dict[comp.label_id.text]=comp






