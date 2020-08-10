import anvil.microsoft.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import io
import uuid
import datetime
import mistune

@anvil.server.callable
def save_report(report_id, schema, specs, data_dicts):
    
  row=app_tables.reports.get(report_id=report_id)
  
  if not row:
    report_id=str(uuid.uuid4())
    app_tables.reports.add_row(report_id=report_id, title=schema['title'], 
                               last_modified=datetime.datetime.now(),
                               schema=schema, charts=specs, datasets=data_dicts)
    
  else:
    row.update(title=schema['title'], schema=schema, charts=specs, datasets=data_dicts)

@anvil.server.callable
def return_datasets(files):
  
  data_dicts={}
  for file in files:   
    df=pd.read_csv(io.BytesIO(file.get_bytes()))
    data_dict=df.to_dict(orient="records")
    data_dicts[file.name]=data_dict
    
  return data_dicts

def convert_markdown(text):
  return mistune.markdown(text, escape=False)

@anvil.server.callable
def make_html_report(report_id):
  
  report=app_tables.reports.get(report_id=report_id)
  schema=report['schema']
  charts=report['charts']
  datasets=report['datasets']
   
  #column_panel.tag.title=schema['title']
  #main=column_panel.parent
  #main.tag.form_dict={}
  #column_panel.tag.id=schema['id']
  
  html="""
<!DOCTYPE html>
<html>
<style>
.center {
  margin: auto;
  width: 50%;
}
</style>
<head>
  <!-- Import Vega & Vega-Lite (does not have to be from CDN) -->
<script src="https://cdn.jsdelivr.net/npm/vega@5.10.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.7.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.5.1"></script>
<script>
var opts={"renderer": "svg", "mode": "vega-lite", "actions": {"export": true, "source": false, "editor": false, "compiled": false}}  
</script>
</head>
<body>
<div class="center">
"""
  
  for section_schema in schema['widgets']:
    
    html+=f"<h2>{section_schema['title']}</h2>"
        
    for widget_schema in section_schema['widgets']:
      
      if widget_schema['type']=='chart':
        
        spec=charts[str(widget_schema['id'])]
        
        data_name=spec['data'].get('name', None)
        data_values=datasets.get(data_name, None)
        
        if data_name and data_values:
          print("move datasets to global var?")
          html+=gen_vega_vis_named_data(widget_schema['id'], spec, data_name, data_values)
          
        else: #not data_name and not data_values:
          html+=gen_vega_vis_no_named_data(widget_schema['id'], spec)
          
          
      elif widget_schema['type']=='markdown':
        
        html+=convert_markdown(widget_schema['text'])
        
  
  html+="</div></body></html>"
  
  
  m=anvil.BlobMedia('text/html', html.encode(), name=report['title']+'.html')
  
  return m
  
  
      
def gen_vega_vis_named_data(div_id, spec, data_name, data_values):
  
  html=f"""
<p>
<div id=vis{div_id}></div>

<script type="text/javascript">
  var spec = {spec};
  var data_name = "{data_name}";
  var data_values = {data_values};
  vegaEmbed('#vis{div_id}', spec, opts).then(res => 
                                                res.view
                                                .insert(data_name, data_values)
                                                .resize()
                                                .run()
                                                );

</script>
</p>
  """

  return html


def gen_vega_vis_no_named_data(div_id, spec):
  
  html=f"""
<div id="vis{div_id}"></div>

<script type="text/javascript">
  var spec = {spec};
  vegaEmbed('#vis{div_id}', spec, opts)
</script>
  """

  return html
  
 
  

  
  
  
  
  
  
  
  
  