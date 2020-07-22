from ._anvil_designer import channelTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#import reports.widgets.chart_utilities.channel.bin as mybin
from ..bin import bin
from ..sort import sort
from ..axis import axis
from ..legend import legend

class channel(channelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_channel.text=properties['channel_name']
    
    if properties['channel_name']=='color':
      self.button_legend.visible=True

  def button_bin_click(self, **event_args):
    
    bins_content=bin()
    c=confirm(bins_content, large=True, 
              buttons=[('apply', 'apply'),('cancel', 'cancel')],
                      title="Bin properties")
    
  def button_sort_click(self, **event_args):
    
    sort_content=bin()
    c=confirm(sort_content, large=True, 
              buttons=[('apply', 'apply'),('cancel', 'cancel')],
                      title="Sort properties")
    
  def button_axis_click(self, **event_args):
    
    axis_content=axis()
    c=confirm(axis_content, large=True, 
              buttons=[('apply', 'apply'),('cancel', 'cancel')],
                      title="Axis properties")
    
  def button_legend_click(self, **event_args):
    
    legend_content=bin()
    c=confirm(legend_content, large=True, 
              buttons=[('apply', 'apply'),('cancel', 'cancel')],
                      title="Legend properties")
