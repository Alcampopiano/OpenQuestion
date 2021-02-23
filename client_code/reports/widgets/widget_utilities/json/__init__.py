from ._anvil_designer import jsonTemplate
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
from anvil.js.window import JSONEditor
import anvil.http

class json(jsonTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)
    self.tag.form_shown=False
    
  def set_editor(self, spec):
    self.editor.set(spec)
    
  def on_editor_change(self, spec):
    print('asdf')
    self.tag.chart.tag.vl_spec=spec
    self.tag.chart.vega_embed()
    
  def form_show(self, **event_args):

    if not self.tag.form_shown:
      
      self.tag.form_shown=True
      
      spec=self.tag.chart.tag.vl_spec
      
      schema = anvil.http.request('https://vega.github.io/schema/vega-lite/v4.json', 
                                           json=True)
      
      # color-hex format not supported so changing it 
      # and moving on with my life 
      schema['definitions']["HexColor"]['format']="uri"
      
      options = {
      'schema': schema,
      'mode': 'code',
      'modes': ['code', 'tree'],
      'onChange': self.on_editor_change
      }

      container = anvil.js.get_dom_node(self)
      self.editor = JSONEditor(container, options, spec)
      #self.editor._onChange(self.on_editor_change)


      

