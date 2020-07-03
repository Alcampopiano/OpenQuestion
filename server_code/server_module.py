import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def get_forms():
  
  forms=[dict(row) for row in app_tables.forms.search()]
  
  return forms

@anvil.server.callable
def save_schema(form_id, schema):
  
  row=app_tables.forms.get(form_id=form_id)
  row.update(schema=schema, last_modified=datetime.now())
  
  


