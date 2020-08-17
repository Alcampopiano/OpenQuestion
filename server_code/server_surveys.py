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
  return u['admin']

# @anvil.server.callable(require_user = validate_user)
# def test():
#   print("passed the test!")


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
    
  return mistune.markdown(row['thank_you_msg'], escape=False)
    
    
@anvil.server.callable
def convert_markdown(text):
  return mistune.markdown(text, escape=False)
  

def check_opening_closing_dates(opening_date, closing_date):
  
  current_date = datetime.now(anvil.tz.tzlocal()) #aware_local
  #print(current_date)
  #print(opening_date)
  #print(closing_date)

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
def get_form(form_id, current_date, preview_link_clicked):
    
  row=app_tables.forms.get(form_id=form_id)

  print('getting aware datetime from server rather than passing client aware date')
  print('not sure if this is the correct way to do it')
  
  # let admins preview otherwise, check for valid dates
  if not anvil.users.get_user()['admin'] or \
    (anvil.users.get_user()['admin'] and preview_link_clicked):
    check_opening_closing_dates(row['opening_date'], row['closing_date'])
        
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
                
    default_thank_you="Thank you! Your responses have been submitted."
    
    app_tables.forms.add_row(form_id=form_id, last_modified=datetime.now(), 
                             schema=schema, title=schema['title'], thank_you_msg=default_thank_you)
           
  else:
    form_id=str(form_id)
    row=app_tables.forms.get(form_id=form_id)
    row.update(title=schema['title'], schema=schema, last_modified=datetime.now())
    
  return form_id
  
  
@anvil.server.callable
def save_survey_settings(form_id, settings_dict):
  row=app_tables.forms.get(form_id=form_id)
  row.update(**settings_dict)
  
  


