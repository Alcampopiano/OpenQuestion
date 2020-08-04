from ._anvil_designer import jsonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class json(jsonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.tag.form_shown=False

  def on_editor_change(self, spec):
    #self.tag.chart.vl_spec=spec
    self.tag.chart.tag.vl_spec=spec
    self.tag.chart.vega_embed()
    
  def form_show(self, **event_args):

    if not self.tag.form_shown:
      print('here')
      self.tag.form_shown=True
      spec=self.tag.chart.tag.vl_spec
      #self.call_js("get_schema", spec, self, self.tag.parent)
      self.call_js("make_editor", spec, self, self.tag.parent)
            