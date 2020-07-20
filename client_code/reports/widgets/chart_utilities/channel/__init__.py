from ._anvil_designer import channelTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class channel(channelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_channel.text=properties['channel_name']
    
    if properties['channel_name']=='color':
      self.button_legend.visible=True