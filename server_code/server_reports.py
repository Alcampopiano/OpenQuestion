import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import altair as alt
import pandas as pd
import io

@anvil.server.callable
def get_columns(file):
  df=pd.read_csv(io.BytesIO(file.get_bytes())) #index_col=0
  
  return list(df.columns)

  

@anvil.server.callable
def make_chart(spec, dataset):
  
    df=pd.read_csv(io.BytesIO(dataset.get_bytes()), index_col=0)
    df_dicts=df.reset_index().to_dict('records')
    spec=adjust_spec(spec)

    spec["$schema"]="https://vega.github.io/schema/vega-lite/v4.json"
    spec['data']={'name': 'data'}
    spec['datasets']={spec['data']['name']: df_dicts}    
  
      
    return spec
  
  
  
def adjust_spec(spec):

    for k, v in list(spec.items()):

        #print(k,v)

        if type(spec[k]) is dict and spec[k] != {}:

            #print(spec[k])

            adjust_spec(spec[k])

        elif spec[k] == '' or spec[k] == {}:
            #print('here')

            del spec[k]

    return spec
      
      
 
  

  
  
  
  
  
  
  
  
  