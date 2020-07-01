import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_forms():
  
  forms=[dict(row) for row in app_tables.forms.search()]
  
  return forms


