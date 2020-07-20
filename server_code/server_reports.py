import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import altair as alt

@anvil.server.callable
def make_chart():
  
    source = pd.DataFrame({
        'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
    })
    
    c=alt.Chart(source).mark_bar().encode(
        x='a',
        y='b'
    )
        
    #print(c.to_dict())
    return c.to_dict()