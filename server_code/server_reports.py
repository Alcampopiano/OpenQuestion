import anvil.microsoft.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import io
import uuid

@anvil.server.callable
def save_report(report_id, specs, data_dicts):
    
  row=app_tables.reports.get(uuid=report_id)
  
  if not row:
    report_id=str(uuid.uuid4())
    app_tables.reports.add_row(uuid=report_id, specs=specs, datasets=data_dicts)
    
  else:
    row.update(specs=specs, datasets=data_dicts)

@anvil.server.callable
def return_datasets(files):
  
  data_dicts={}
  for file in files:   
    df=pd.read_csv(io.BytesIO(file.get_bytes()))
    data_dict=df.to_dict(orient="records")
    data_dicts[file.name]=data_dict
    
  return data_dicts

# @anvil.server.callable
# def get_dataset():
#   m=app_tables.datasets.get(title="my_survey_data.csv")['media']
#   df=pd.read_csv(io.BytesIO(m.get_bytes()))
#   data_dict=df.to_dict(orient="records")
  
#   return data_dict
    
# @anvil.server.http_endpoint('/get_dataset', authenticate_users=True, require_credentials=True)
# def get_dataset():
  
#   dataset=app_tables.datasets.get(title='my_survey_data.csv')
#   r = anvil.server.HttpResponse()
#   r.headers['content-disposition'] = 'attachment; filename="my_survey_data.csv"'
#   r.body = anvil.BlobMedia('text/csv', content=dataset['media'].get_bytes())
#   b=dataset['media']
  
#   return b #r

# @anvil.server.callable
# def get_columns(file):
#   df=pd.read_csv(io.BytesIO(file.get_bytes())) #index_col=0
  
#   return list(df.columns)

# @anvil.server.callable
# def make_chart(spec, dataset):
  
#     df=pd.read_csv(io.BytesIO(dataset.get_bytes()), index_col=0)
#     df_dicts=df.reset_index().to_dict('records')
#     spec=adjust_spec(spec)

#     spec["$schema"]="https://vega.github.io/schema/vega-lite/v4.json"
#     spec['data']={'name': 'data'}
#     spec['datasets']={spec['data']['name']: df_dicts}    
  
      
#     return spec
  
  
# def adjust_spec(spec):

#     for k, v in list(spec.items()):

#         #print(k,v)

#         if type(spec[k]) is dict and spec[k] != {}:

#             #print(spec[k])

#             adjust_spec(spec[k])

#         elif spec[k] == '' or spec[k] == {}:
#             #print('here')

#             del spec[k]

#     return spec
      
      
 
  

  
  
  
  
  
  
  
  
  