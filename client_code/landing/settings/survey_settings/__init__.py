from ._anvil_designer import survey_settingsTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
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
    schema_settings=row['schema']['settings']
    self.date_picker_opening_date.date=row['opening_date']
    self.date_picker_closing_date.date=row['closing_date']
    self.text_area_thank_you_msg.text=schema_settings['thank_you_msg']
    self.text_box_survey_color.text=schema_settings['survey_color']
    
  def button_apply_click(self, **event_args):
    opening=self.date_picker_opening_date.date
    closing=self.date_picker_closing_date.date
    thank_you=self.text_area_thank_you_msg.text
    survey_color=self.text_box_survey_color.text
    
    settings_in_schema=dict(survey_color=survey_color,
                            thank_you_msg=thank_you
                           )
    
    form_id=self.tag.row['form_id']
    settings_in_datatable=dict(opening_date=opening,
                               closing_date=closing,
                              )
    
    anvil.server.call('save_survey_settings', form_id, settings_in_schema,
                      settings_in_datatable)
      
  def button_cancel_click(self, **event_args):
    open_form('landing.select_action_survey')

  def button_delete_click(self, **event_args):
    
    title=self.tag.row['title']
    c=confirm('', title=f"Are you sure you want to delete {title}?", 
              buttons=[('Yes', 'yes'), ('Cancel', 'cancel')])
    
    if c=='yes':
      anvil.server.call('delete_survey', self.tag.row['form_id'])
      Notification('', title='Deleted').show()
      open_form('landing.select_action_survey')

  def link_home_click(self, **event_args):
    open_form('landing.select_action_survey')
    



