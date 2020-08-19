from ._anvil_designer import survey_settingsTemplate
from anvil import *
import anvil.server
import anvil.microsoft.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class survey_settings(survey_settingsTemplate):
  def __init__(self, row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_survey.text=f"Survey settings: {row['title']}"
    self.tag.row=row
    self.date_picker_opening_date.date=row['opening_date']
    self.date_picker_closing_date.date=row['closing_date']
    self.text_area_thank_you_msg.text=row['thank_you_msg']
    
  def button_apply_click(self, **event_args):
    opening=self.date_picker_opening_date.date
    closing=self.date_picker_closing_date.date
    thank_you=self.text_area_thank_you_msg.text
    form_id=self.tag.row['form_id']
    settings_dict=dict(opening_date=opening,
                      closing_date=closing,
                      thank_you_msg=thank_you
                      )
    
    anvil.server.call('save_survey_settings', form_id, settings_dict)
      
  def button_cancel_click(self, **event_args):
    open_form('landing.select_action_survey')

  def button_delete_click(self, **event_args):
    
    title=self.tag.row['title']
    c=confirm('', title=f"Are you sure you want to delete {title}?", 
              buttons=[('Yes', 'yes'), ('Cancel', 'cancel')])
    
    if c=='yes':
      anvil.server.call('delete_survey', self.tag.row['form_id'])
      Notification('', title='Deleted').show()

  def link_back_click(self, **event_args):
    open_form('landing.select_action_survey')


  def link_home_click(self, **event_args):
    open_form('landing.main')





