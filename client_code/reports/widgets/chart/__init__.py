from ._anvil_designer import chartTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class chart(chartTemplate):
  def __init__(self, section, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.chart_display.vl_spec = anvil.server.call('make_chart')
    
    # Any code you write here will run when the form opens.
    from ..toolbar import toolbar
    toolbar=toolbar(align='left', section=section, parent=self)
    
    self.add_component(toolbar)
