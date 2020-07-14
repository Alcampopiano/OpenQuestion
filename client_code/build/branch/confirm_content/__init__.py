from ._anvil_designer import confirm_contentTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class confirm_content(confirm_contentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def add_click(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass

  def widget_change(self, **event_args):
    """This method is called when an item is selected"""
    
    if self.drop_down_widgets.selected_value.__name__ in \
      ('drop_down', 'radio_button'):
      
      items=self.drop_down_widgets.selected_value.text_area_options.text.split('\n')
      val_comp=DropDown(items=items)
      self.flow_panel_build_condition.add_component(val_comp)
      
    elif self.drop_down_widgets.selected_value.__name__ == 'date':
      val_comp=DatePicker()
      self.flow_panel_build_condition.add_component(val_comp)
      


