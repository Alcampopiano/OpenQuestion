import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import uuid 
import mistune
import pandas as pd
import io

def validate_user(u):
  return u #u['admin']

@anvil.server.callable(require_user = validate_user)
def delete_survey(form_id):
  
  row=app_tables.forms.get(form_id=form_id)
  row.delete()

@anvil.server.callable()
def str_to_date_obj(date_str, date_format):
  
  # until strptime is implemented on the client (forcing to date until time is allowed as an option)
  return datetime.strptime(date_str, date_format).date()
  
  
@anvil.server.callable
def submit_data(cols, data, url_hash):
  
#   print(url_hash)
#   print(url_hash.keys())
  
  meta_hash_keys=[k for k in url_hash.keys()]
  meta_hash_vals=[v for v in url_hash.values()]

  cols+=meta_hash_keys
  data+=meta_hash_vals

  form_id=url_hash['form_id']
  
  df_new=pd.DataFrame([data], columns=cols)
  df_new.columns=pd.io.parsers.ParserBase({'names':df_new.columns})._maybe_dedup_names(df_new.columns)
  row=app_tables.forms.get(form_id=form_id)
  
  if not row['submissions']:
    
    # fix from forum since suddently we need bytes
    # USE FIX FROM BRIDGET
    #####
    csv_data=df_new.to_csv()
    csv_data=csv_data.encode()
    #csv_data = bytes(csv_data, 'utf-8') # fix

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
        
  return mistune.markdown(row['schema']['settings']['thank_you_msg'], escape=False)
    
    
@anvil.server.callable(require_user = validate_user)
def convert_markdown(text):
  return mistune.markdown(text, escape=False)
  

def check_opening_closing_dates(opening_date, closing_date):
  
  # getting aware datetime from server rather than passing client aware date
  current_date = datetime.now(anvil.tz.tzlocal()) #aware_local

  if opening_date and closing_date and (opening_date < current_date < closing_date):
    pass
  
  elif (opening_date and current_date>opening_date) and not closing_date:
    pass
  
  elif (closing_date and current_date<closing_date) and not opening_date:
    pass
    
  elif not opening_date and not closing_date:
    pass
  
  else:
    raise Exception("survey inactive")
    
    
@anvil.server.callable
def get_form(url_hash):
      
  #print(url_hash)
  form_id=url_hash['form_id']
  preview_link_clicked=url_hash.get('preview', False)
  
  row=app_tables.forms.get(form_id=form_id)
  
  # let admins preview otherwise, check for valid dates
  if not anvil.users.get_user() or \
    (anvil.users.get_user() and not preview_link_clicked):
    check_opening_closing_dates(row['opening_date'], row['closing_date'])
        
  return row['schema']
  

@anvil.server.callable(require_user = validate_user)
def get_forms():
  
  forms=[dict(row) for row in app_tables.forms.search()]
  
  return forms

@anvil.server.callable(require_user = validate_user)
def get_reports():
  
  reports=[dict(row) for row in app_tables.reports.search()]
  
  return reports

@anvil.server.callable(require_user = validate_user)
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
  
  
@anvil.server.callable(require_user = validate_user)
def save_survey_settings(form_id, settings_in_schema, settings_in_datatable):
  
  row=app_tables.forms.get(form_id=form_id)
  schema=row['schema']
  schema['settings'].update(**settings_in_schema)
  row.update(schema=schema)
  row.update(**settings_in_datatable)
  
  


