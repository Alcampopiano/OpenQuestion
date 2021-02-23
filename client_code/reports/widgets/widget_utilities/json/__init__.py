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

class json(jsonTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)
    self.tag.form_shown=False

  def on_editor_change(self, spec):
    self.tag.chart.tag.vl_spec=spec
    self.tag.chart.vega_embed()
    
  def form_show(self, **event_args):

    if not self.tag.form_shown:
      
      self.tag.form_shown=True
      
      spec=self.tag.chart.tag.vl_spec
      
      #get schema from anvil.https call
      options = {
      'schema': schema,
      'mode': 'code',
      'modes': ['code', 'tree'],
      'onChange': self.on_editor_change 
    }

    container = anvil.js.get_dom_node(self)
    self.editor = JSONEditor(container, options, self.spec)
      #self.call_js("make_editor", spec, self, self.tag.parent)            
