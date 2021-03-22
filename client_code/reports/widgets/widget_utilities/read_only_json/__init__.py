from ._anvil_designer import read_only_jsonTemplate
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
import json as json_lib

class read_only_json(read_only_jsonTemplate):
  def __init__(self, **properties):

    self.init_components(**properties)
    
  def set_json_editor(self, spec, **event_args):
    
    options = {
    #'schema': get_open_form().tag.vl_schema,
    'mode': 'code',
    'modes': ['code','view'],
    }

    container = anvil.js.get_dom_node(self)
    self.editor = JSONEditor(container, options, spec)

      

