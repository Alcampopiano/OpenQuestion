from ._anvil_designer import survey_settingsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class survey_settings(survey_settingsTemplate):
  def __init__(self, row, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.date_picker_opening_date.date=row['opening_date']
    self.date_picker_closing_date.date=row['closing_date']
    self.text_area_thank_you_msg.text=row['thank_you_msg']


#   def save_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     print('call save settings surver')

