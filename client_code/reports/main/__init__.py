from ._anvil_designer import mainTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import reports
from .. import widgets
from ...utilities import augment

class main(mainTemplate):
  def __init__(self, row=None, **properties):

    self.init_components(**properties)
    
    file_loader=FileLoader(multiple=True, file_types='.csv')
    file_loader.set_event_handler('change', self.file_loader_change)
    augment.add_event(file_loader, 'click')
    self.tag.file_loader=file_loader
    
    self.tag.row=row
    save_button=Button(text='save', role='primary-color')
    save_button.set_event_handler('click', self.save_click)
    self.add_component(save_button)
      
    if row:
      self.tag.id=row['report_id']
      self.tag.data_dicts=row['datasets']
      self.link_datasets.text=str(len(self.tag.data_dicts))
      self.tag.num_widgets=row['schema']['num_widgets']
      self.text_box_title.text=row['title']
      reports.build_report(row['schema'], row['charts'], self.column_panel)
      
    else:
      
      self.tag.form_dict={}
      self.tag.data_dicts={}
      self.tag.id=None
      self.tag.num_widgets=0  
      
  def save_click(self, **event_args):
    schema, chart_dict=reports.build_schema(self.column_panel)
    datasets=self.tag.data_dicts
    
    report_id=anvil.server.call('save_report', 
                      self.tag.id, 
                      schema, chart_dict, datasets)
    
    self.tag.id=report_id
    
  def form_show(self, **event_args):
    
    if not self.tag.row:
      self.section_widget_click()
      
    else:
      
      last_section=self.column_panel.get_components()[-1]
      last_section.section_select()
      
          
  def link_landing_click(self, **event_args):
     open_form('landing.select_action')
    
  def markdown_widget_click(self, **event_args):
    """This method is called when the link is clicked"""
    comp=widgets.markdown(section=self.tag.active_section)
    self.tag.active_section.column_panel.add_component(comp)
    #self.color_rows(self.tag.active_section)
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
      #self.color_rows(self.tag.active_section)
      comp.label_id.text=self.tag.num_widgets
      self.tag.num_widgets+=1
      self.tag.form_dict[comp.label_id.text]=comp
      
    else:
      self.link_datasets_click()
      #alert("click the databse icon in the top nav bar", title="Please load datasets first")
    
  def file_loader_change(self, files, **event_args):
    
    if files:
      data_dicts=anvil.server.call('return_datasets', files)
      self.tag.data_dicts=data_dicts
      
    self.link_datasets.text=str(len(self.tag.data_dicts))

  def link_datasets_click(self, **event_args):
    self.tag.file_loader.trigger('click')

  def link_download_click(self, **event_args):
    
    if not self.tag.id:
      self.save_click()
      
    m=anvil.server.call('make_html_report', self.tag.id)
    download(m)

  def link_landing_report_click(self, **event_args):
     open_form('landing.select_action_report')
      
  def link_home_click(self, **event_args):
    open_form('landing.main')












