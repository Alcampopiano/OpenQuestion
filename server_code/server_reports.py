import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import altair as alt
import pandas as pd

@anvil.server.callable
def make_chart(spec):
  
    df = pd.DataFrame({
        'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
    })
    
    df_dicts=df.to_dict('records')

    
    spec['data']={'name': 'data'}
    spec['datasets']={spec['data']['name']: df_dicts}
    
    return spec