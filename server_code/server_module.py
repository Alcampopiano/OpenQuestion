import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import uuid 
import mistune

@anvil.server.callable
def convert_markdown(text):
  return mistune.markdown(text, escape=False)
  

@anvil.server.callable
def get_form(form_id):
  
  row=app_tables.forms.get(form_id=form_id)
  return row['schema']
  

@anvil.server.callable
def get_forms():
  
  forms=[dict(row) for row in app_tables.forms.search()]
  
  return forms

@anvil.server.callable
def save_schema(form_id, schema):
  
  if not form_id:
    form_id=str(uuid.uuid4())
                
    app_tables.forms.add_row(form_id=form_id, last_modified=datetime.now(), 
                             schema=schema, title=schema['title'])
           
  else:
    form_id=str(form_id)
    row=app_tables.forms.get(form_id=form_id)
    row.update(title=schema['title'], schema=schema, last_modified=datetime.now())
    
  return form_id
  
  


