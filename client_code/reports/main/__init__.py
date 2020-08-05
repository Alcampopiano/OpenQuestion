from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from ... import charts
from .. import widgets

class main(mainTemplate):
  def __init__(self, row=None, **properties):

    self.init_components(**properties)
    
    #self.tag.row=row
    self.tag.form_dict={}
    #self.tag.num_widgets=0
    save_button=Button(text='save', role='primary-color')
    save_button.set_event_handler('click', self.save_click)
    self.add_component(save_button)
      
    if row:
      print('call load method in report module')
#       self.tag.id=row['form_id']
#       self.preview_link.url=anvil.server.get_app_origin() + '#' + row['form_id']
#       self.tag.num_widgets=row['schema']['num_widgets']
#       self.text_box_title.text=row['title']
#       build.build_form(row['schema'], self.column_panel)
      
    else:
      self.tag.data_dicts={}
      self.tag.id=None
      self.tag.num_widgets=0  
      
  def save_click(self, **event_args):
    print('call save method in report module')
#     report_id=1
#     specs={}
#     for widget_id, chart in enumerate(self.tag.chart_wigets):
#       spec=chart.tag.vl_spec
#       specs[str(widget_id)]=spec
      
#     datasets=self.tag.data_dicts
#     anvil.server.call('save_report', '1', specs, datasets)
    
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
    
    if self.tag.data_dicts:
      comp=widgets.chart(section=self.tag.active_section)
      self.tag.active_section.column_panel.add_component(comp)
      self.color_rows(self.tag.active_section)
      comp.label_id.text=self.tag.num_widgets
      self.tag.num_widgets+=1
      self.tag.form_dict[comp.label_id.text]=comp
      
    else:
      alert("click the databse icon in the top nav bar", title="Please load datasets first")
    
  def file_loader_change(self, files, **event_args):
    
    if files:
      data_dicts=anvil.server.call('return_datasets', files)
      self.tag.data_dicts=data_dicts
      
    self.file_loader.text=str(len(self.tag.data_dicts))











