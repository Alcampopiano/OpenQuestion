import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import uuid 
import mistune
import pandas as pd
import io

@anvil.server.callable
def str_to_date_obj(date_str, date_format):
  
  # until strptime is implemented on the client (forcing to date until time is allowed as an option)
  return datetime.strptime(date_str, date_format).date()
  
  
@anvil.server.callable
def submit_data(cols, data, form_id):
  
  df_new=pd.DataFrame([data], columns=cols)
  df_new.columns=pd.io.parsers.ParserBase({'names':df_new.columns})._maybe_dedup_names(df_new.columns)
  row=app_tables.forms.get(form_id=form_id)
  
  if not row['submissions']:
    
    # fix from forum since suddently we need bytes
    # USE FIX FROM BRIDGET
    #####
    csv_data=df_new.to_csv()
    csv_data = bytes(csv_data, 'utf-8') # fix
    #####
    
    m=anvil.BlobMedia('text/csv', csv_data, name='records.csv')
    row.update(submissions=m)
    
  else:
    m_old=row['submissions']
    df_old=pd.read_csv(io.BytesIO(m_old.get_bytes()), index_col=0) # index_col=0
    df=pd.concat([df_old, df_new], axis=0)
    df=df.reset_index(drop=True)
    
    # fix from forum since suddently we need bytes
    # USE FIX FROM BRIDGET
    #####
    csv_data=df.to_csv()
    csv_data=csv_data.encode()
    #csv_data = bytes(csv_data, 'utf-8')
    #####
    
    m=anvil.BlobMedia('text/csv', csv_data, name='records.csv')
    row.update(submissions=m)
    
    
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
def get_reports():
  
  reports=[dict(row) for row in app_tables.reports.search()]
  
  return reports

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
  
  


