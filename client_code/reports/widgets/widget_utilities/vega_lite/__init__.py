from ._anvil_designer import vega_liteTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class vega_lite(vega_liteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.tag.vl_spec={
    "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
    "description": "A simple bar chart with embedded data.",
    "data": {"name": ""},
    "mark": "bar",
    "encoding": {
      "x": {"field": "Year", "type": "nominal"},
      "y": {"field": "Score", "type": "quantitative", 
            "aggregate": "sum"}
    }
  }
  
  def form_show(self, **event_args):
    
    spec=self.tag.vl_spec
    data_name=spec['data'].get('name', None)
    data_values=get_open_form().tag.data_dicts.get(data_name, None)
    
    if data_name and data_values:
      self.call_js('vega_embed_named_data', self.tag.vl_spec, 
                 data_name, data_values)
      
    else: #not data_name and not data_values:
        self.call_js('vega_embed_no_named_data', self.tag.vl_spec)
      
    