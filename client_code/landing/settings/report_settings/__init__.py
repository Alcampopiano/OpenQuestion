from ._anvil_designer import report_settingsTemplate
from anvil import *
import anvil.server
import anvil.microsoft.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class report_settings(report_settingsTemplate):
  def __init__(self, row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_report.text=f"Report settings: {row['title']}"
    self.tag.row=row
    
  def button_cancel_click(self, **event_args):
    open_form('landing.select_action_report')

  def button_delete_click(self, **event_args):
    
    title=self.tag.row['title']
    c=confirm('', title=f"Are you sure you want to delete {title}?", 
              buttons=[('yes', 'yes'), ('cancel', 'cancel')])
    
    if c=='yes':
      anvil.server.call('delete_report', self.tag.row['form_id'])
      Notification('', title='Deleted').show()

  def link_back_click(self, **event_args):
    open_form('landing.select_action_report')

  def link_home_click(self, **event_args):
    open_form('landing.main')