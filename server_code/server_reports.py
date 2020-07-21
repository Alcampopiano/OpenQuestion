import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import altair as alt
import pandas as pd

@anvil.server.callable
def make_chart(chart_dict):
  
    df = pd.DataFrame({
        'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
    })
    
    marks={'bar': alt.mark_bar, 'line': alt.mark_line, 'area': alt.mark_area}
    
    c=alt.Chart(source).mark_bar(tooltip=True).encode(
        x='a',
        y='b'
    ).properties(width=500)
    
    
        
    #print(c.to_dict())
    return c.to_dict()