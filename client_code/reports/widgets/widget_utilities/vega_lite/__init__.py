from ._anvil_designer import vega_liteTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import vegaEmbed

class vega_lite(vega_liteTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)
    
    self.tag.form_shown=False

    self.tag.vl_spec={
  "data": {
    "url": "https://vega.github.io/vega-lite/data/cars.json" 
  },
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "mark": "circle",
  "width": 310,
  "height": 300,
  "encoding": {
    "x": {
      "type": "quantitative",
      "field": "Horsepower"
    },
    "y": {
      "type": "quantitative",
      "field": "Miles_per_Gallon"
    },
    "color": {
      "type": "nominal",
      "field": "Origin"
    },
    "tooltip": [{"field": "Acceleration", "title": "Acceleration"}]
  }
}
  
  def form_show(self, **event_args):
    
    if not self.tag.form_shown:
      self.tag.form_shown=True
      self.vega_embed()
      
  def vega_embed(self, **event_args):
    
    spec=self.tag.vl_spec
    data_name=spec['data'].get('name', None)
    data_values=get_open_form().tag.data_dicts.get(data_name, None)
    
    el = anvil.js.get_dom_node(self)
    embedded = vegaEmbed(el, spec)
    
    if data_name and data_values:

      view = embedded.view
      view.insert(data_name, data_values)           
      view.resize()
      view.run()
      
      #self.call_js('vega_embed_named_data', self.tag.vl_spec, 
      #               data_name, data_values)
      
    else:
      view = embedded.view
      #self.call_js('vega_embed_no_named_data', self.tag.vl_spec)
      
    self.tag.view=view
        
    
        
    