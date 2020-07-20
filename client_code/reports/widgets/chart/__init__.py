from ._anvil_designer import chartTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..chart_utilities.channel import channel

class chart(chartTemplate):
  def __init__(self, section, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    #self.chart_display.vl_spec = anvil.server.call('make_chart')
    
    # Any code you write here will run when the form opens.
    from ..toolbar import toolbar
    toolbar=toolbar(align='left', section=section, parent=self)
    
    self.add_component(toolbar)

  def channel_but_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    channel_labs=[c.text for c in self.flow_panel_channels.get_components() if c.checked]
    
    for channel_name in channel_labs:
      chan=channel(channel_name=channel_name)
      self.column_panel.add_component(chan)
      

  def channel_check_changed(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    
    if event_args['sender'].checked:
      channel_name=event_args['sender'].text
      chan=channel(channel_name=channel_name)
      self.column_panel.add_component(chan)
      
    else:
      channel_name=event_args['sender'].text
      channel_labs=[c.remove_from_parent() for c in self.column_panel.get_components() 
                    if c.label_channel.text==channel_name]

      


      




