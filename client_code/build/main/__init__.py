from ._anvil_designer import mainTemplate
from anvil import *
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import widgets
from ... import build
from ... import form

class main(mainTemplate):
  def __init__(self, row=None, **properties):

    self.init_components(**properties)

    self.tag.row=row
    self.tag.form_dict={}
    save_button=Button(text='save', role='primary-color')
    save_button.set_event_handler('click', self.save_click)
    self.add_component(save_button)
    
    if row:
      self.tag.id=row['form_id']
      self.preview_link.url=anvil.server.get_app_origin() + '#?form_id=' + row['form_id'] + '&preview=true'
      self.tag.num_widgets=row['schema']['num_widgets']
      self.text_box_title.text=row['title']
      build.build_form(row['schema'], self.column_panel)
      
    else:
      self.tag.id=None
      self.tag.num_widgets=0
      
  def save_click(self, **event_args):
    schema=build.build_schema(self.column_panel)
    form_id=anvil.server.call('save_schema', self.tag.id, schema)
    self.tag.id=form_id
    self.preview_link.url=anvil.server.get_app_origin() + '#?form_id=' + form_id + '&preview=true'

  def form_show(self, **event_args):
    
    if not self.tag.row:
      #self.section_widget_click()
      self.add_widget_click(self.link_section)

    else:
      
      for section in self.column_panel.get_components():
        self.color_rows(section)
        
      section.section_select()
      
      
  def color_rows(self, section, **event_args):
            
    for i, comp in enumerate(section.column_panel.get_components()):

      if not i%2:
        comp.background='theme:Gray 100'
        
      else:
        comp.background='white'
        
          
  def link_landing_survey_click(self, **event_args):
     open_form('landing.select_action_survey')
      
  def link_home_click(self, **event_args):
    open_form('landing.main')

  def preview_link_click(self, **event_args):
    
    if not self.preview_link.url:
      Notification('',title='Please save the form first').show()

    else:
      schema=build.build_schema(self.column_panel)
      anvil.server.call('save_schema', self.tag.id, schema)
      
  # from stu    
  def add_widget_click(self, sender, **event_args):
    widget_type=sender.text
    
    if widget_type != 'section':
      
      comp = getattr(widgets, widget_type)(section=self.tag.active_section)
      print(comp)      
      self.tag.active_section.column_panel.add_component(comp)

    else:
      comp = getattr(widgets, widget_type)()
      print(comp)
      self.column_panel.add_component(comp)

    comp.label_id.text=self.tag.num_widgets
    self.tag.num_widgets+=1
    self.tag.form_dict[comp.label_id.text]=comp
    comp.scroll_into_view()
    self.color_rows(self.tag.active_section)

#   def section_widget_click(self, **event_args):
#     section=widgets.section()
#     self.column_panel.add_component(section)
#     section.label_id.text=self.tag.num_widgets
#     self.tag.num_widgets+=1
#     self.tag.form_dict[section.label_id.text]=section
    
#   def text_box_widget_click(self, **event_args):
#     comp=widgets.text_box(section=self.tag.active_section)
#     self.tag.active_section.column_panel.add_component(comp)
#     self.color_rows(self.tag.active_section)
#     comp.label_id.text=self.tag.num_widgets
#     self.tag.num_widgets+=1
#     self.tag.form_dict[comp.label_id.text]=comp

#   def drop_down_widget_click(self, **event_args):
#     comp=widgets.drop_down(section=self.tag.active_section)
#     self.tag.active_section.column_panel.add_component(comp)
#     self.color_rows(self.tag.active_section)
#     comp.label_id.text=self.tag.num_widgets
#     self.tag.num_widgets+=1
#     self.tag.form_dict[comp.label_id.text]=comp

#   def date_widget_click(self, **event_args):
#     comp=widgets.date(section=self.tag.active_section)
#     self.tag.active_section.column_panel.add_component(comp)
#     self.color_rows(self.tag.active_section)
#     comp.label_id.text=self.tag.num_widgets
#     self.tag.num_widgets+=1
#     self.tag.form_dict[comp.label_id.text]=comp

#   def check_box_widget_click(self, **event_args):
#     comp=widgets.check_box(section=self.tag.active_section)
#     self.tag.active_section.column_panel.add_component(comp)
#     self.color_rows(self.tag.active_section)
#     comp.label_id.text=self.tag.num_widgets
#     self.tag.num_widgets+=1
#     self.tag.form_dict[comp.label_id.text]=comp
    
#   def radio_button_widget_click(self, **event_args):
#     comp=widgets.radio_button(section=self.tag.active_section)
#     self.tag.active_section.column_panel.add_component(comp)
#     self.color_rows(self.tag.active_section)
#     comp.label_id.text=self.tag.num_widgets
#     self.tag.num_widgets+=1
#     self.tag.form_dict[comp.label_id.text]=comp
    
#   def markdown_widget_click(self, **event_args):
#     comp=widgets.markdown(section=self.tag.active_section)
#     self.tag.active_section.column_panel.add_component(comp)
#     self.color_rows(self.tag.active_section)
#     comp.label_id.text=self.tag.num_widgets
#     self.tag.num_widgets+=1
#     self.tag.form_dict[comp.label_id.text]=comp
    
#   def text_area_widget_click(self, **event_args):
#     comp=widgets.text_area(section=self.tag.active_section)
#     self.tag.active_section.column_panel.add_component(comp)
#     self.color_rows(self.tag.active_section)
#     comp.label_id.text=self.tag.num_widgets
#     self.tag.num_widgets+=1
#     self.tag.form_dict[comp.label_id.text]=comp
    
#   def slider_widget_click(self, **event_args):
#     comp=widgets.slider(section=self.tag.active_section)
#     self.tag.active_section.column_panel.add_component(comp)
#     self.color_rows(self.tag.active_section)
#     comp.label_id.text=self.tag.num_widgets
#     self.tag.num_widgets+=1
#     self.tag.form_dict[comp.label_id.text]=comp













