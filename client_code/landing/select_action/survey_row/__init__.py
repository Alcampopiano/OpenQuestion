from ._anvil_designer import survey_rowTemplate
from anvil import *
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...settings.survey_settings import survey_settings

class survey_row(survey_rowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_title.text=self.item['title']
    self.button_build.tag.row=self.item
    

  def button_build_form_click(self, **event_args):

    with Notification('', title='please wait...'):
      row=self.button_build.tag.row
      open_form('build.main', row=row)

  def data_click(self, **event_args):

    row=self.button_build.tag.row
    download(row['submissions'])

  def share_click(self, **event_args):
    Notification('should copy the unique url to clipboard', 
                 title="not yet implemented").show()

  def settings_click(self, **event_args):
    row=self.button_build.tag.row
    settings=survey_settings(row=row)
    c=confirm(content=settings, large=True, buttons=[('save', 'save'), ('cancel', 'cancel')])
    
    if c=='save':
      opening=settings.date_picker_opening_date.date
      closing=settings.date_picker_closing_date.date
      thank_you=settings.text_area_thank_you_msg.text
      form_id=self.button_build.tag.row['form_id']
      settings_dict=dict(opening_date=opening,
                        closing_date=closing,
                        thank_you_msg=thank_you
                        )
      
      anvil.server.call('save_survey_settings', form_id, settings_dict)
      row.update(**settings_dict)



  