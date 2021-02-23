import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
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
import ast
import numpy as np
import anvil.http


def validate_user(u):
  return u #u['admin']

@anvil.server.callable(require_user = validate_user)
def get_json_schema():
  
    schema = anvil.http.request('https://vega.github.io/schema/vega-lite/v4.json', 
                                           json=True)
    
    return schema

@anvil.server.callable(require_user = validate_user)
def data_to_spec(survey_row, cols, dataset_name):
  
  dataset=app_tables.forms.get(form_id=survey_row['form_id'])['reports']['datasets'][dataset_name]
  df=pd.DataFrame(dataset)
  
  templates=[t['templates'] for t in app_tables.chart_templates.search()]
    
  col_and_types = df.dtypes[cols]

  rules={}
  for col, dtype in col_and_types.iteritems():
    if dtype=='O':
      rules[col]='n'
    else:
      rules[col]='q'


  new_schemas=[]
  for s in templates:
    if sorted(rules.values()) == sorted(s['rules']):

      str_dict = str(s)
      for k, v in rules.items():
        str_dict = str_dict.replace(f'{{{v}}}', k, 1)

      new_spec=ast.literal_eval(str_dict)
      new_spec["data"].update({"name": dataset_name})
      del new_spec['rules']
      new_schemas.append(new_spec)


  return new_schemas


@anvil.server.callable
def spec_to_template(df, spec):

  key='field'
  rules=[]
  def search_dict_and_create_template(tree):

    for node in tree:
      print(node)
      if node == key and type(tree[node]) is str:

        if df[tree[key]].dtype=='O':
          tree[key]='{n}'
          rules.append('n')
        else:
          tree[key]='{q}'
          rules.append('q')

      elif type(tree[node]) is dict:
        search_dict_and_create_template(tree[node])

      elif type(tree[node]) is list:
        print('in a list')
        for item in tree[node]:
          if type(item) is dict:
            search_dict_and_create_template(item)

    return tree

  spec=search_dict_and_create_template(spec)
  spec["data"]={"name": ''}
  spec['rules']=rules

  return spec

@anvil.server.callable(require_user = validate_user)
def save_report(survey_dict, schema, specs, data_dicts):
      
  survey_row=app_tables.forms.get(form_id=survey_dict['form_id'])  
  report_row=survey_row['reports']
  
  if not report_row:
    #report_id=str(uuid.uuid4())
    report_row=app_tables.reports.add_row(title=schema['title'], 
                               last_modified=datetime.datetime.now(),
                               schema=schema, charts=specs, datasets=data_dicts)
    
    survey_row.update(reports=report_row)
    
  else:
    report_row.update(title=schema['title'], schema=schema, charts=specs, datasets=data_dicts)
    
  return dict(survey_row)

@anvil.server.callable(require_user = validate_user)
def return_datasets(files, survey_dict=None):
  
  data_dicts={}
  for file in files:   
    df=pd.read_csv(io.BytesIO(file.get_bytes()))
    df = df.replace({np.nan: None})
    
    try:
      df=df.drop(columns={'Unnamed: 0'})
    except:
      pass
    
    data_dict=df.to_dict(orient="records")
    data_dicts[file.name]=data_dict
    
    if survey_dict:
      print('officially saving datasets here now')
      survey_row=app_tables.forms.get(form_id=survey_dict['form_id'])
      report_row=survey_row['reports']
      report_row.update(datasets=data_dicts)
    
  return data_dicts

@anvil.server.callable(require_user = validate_user)
def convert_markdown(text):
  return mistune.markdown(text, escape=False)

@anvil.server.callable(require_user = validate_user)
def data_dicts_to_html(data_dicts):
  
  html=''
  for k,v in data_dicts.items():
    html+='<h3>{0}</h3>'.format(k)
    html+=pd.DataFrame.from_records(v).head().to_html(index=False)
    html+='<br><hr><br>'
    
  return convert_markdown(html)
  
@anvil.server.callable(require_user = validate_user)
def make_html_report(survey_row):
  
  report_row=survey_row['reports']
  schema=report_row['schema']
  charts=report_row['charts']
  datasets=report_row['datasets']
  
  # there is obviously a better way of doing this
  # at least I should have this in an external location
  html="""
<!DOCTYPE html>
<html>
<style>

* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

html {
   box-sizing: border-box;
   font-family: sans-serif;
   font-size: 10px;
   -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
	-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
	box-sizing: border-box;
	margin: 0;
	font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
	font-size: 13px;
	line-height: 1.42857143;
	color: #000;
	background-color: #fff;
	position: absolute;
	left: 0px;
	right: 0px;
	top: 0px;
	bottom: 0px;
	overflow: visible;
	padding: 8px;
}

div#notebook {

	-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
	/*font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; */
	color: #000;
	font-size: 15px;
	line-height: 20px;
	width: 100%;
	padding-top: 20px;
    padding-bottom: 50px;
	margin: 0px;
	outline: none;
	-webkit-box-sizing: border-box;
	min-height: 100%;
	overflow: visible;
	border-top: none;

}

@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}


/*
div#notebook-container {

	-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
	font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
	color: #000;
	font-size: 14px;
	line-height: 20px;
	box-sizing: border-box;
	margin-right: auto;
	margin-left: auto;
	width: 768px;
	padding: 15px;
	background-color: #fff;
	min-height: 0;
	box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);

}
*/


/* JL CSS inspection shows just "#notebook-container" w/o "div" */
div#notebook-container {
    padding: 15px 150px 50px 150px; /* JL only used 15px as the only property*/
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
	 width: 1140px; /* doesnt exist here in JL, dynamically adjusted by @media */

}

/* only exists when width is > 768 */
@media (min-width: 768px)
.container {
	width: 768px;
}

.container {
    margin-right: auto;
    margin-left: auto;
}

div.text_cell {
    display: -webkit-box;
    -webkit-box-orient: horizontal;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: horizontal;
    -moz-box-align: stretch;
    display: box;
    box-orient: horizontal;
    box-align: stretch;
    display: flex;
    flex-direction: row;
    align-items: stretch;
}

div.cell {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    border-radius: 2px;
    box-sizing: border-box;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    border-width: 1px;
    border-style: solid;
    border-color: transparent;
    width: 100%;
    padding: 5px;
    margin: 0px;
    outline: none;
    position: relative;
    overflow: visible;
}

/*
div.inner_cell {
-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
color: #000;
font-size: 14px;
line-height: 20px;
box-sizing: border-box;
min-width: 0;
-webkit-box-orient: vertical;
-webkit-box-align: stretch;
display: flex;
flex-direction: column;
align-items: stretch;
-webkit-box-flex: 1;
flex: 1;
}
*/

div.inner_cell {
    min-width: 0;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    -webkit-box-flex: 1;
    -moz-box-flex: 1;
    box-flex: 1;
    flex: 1;
}


.text_cell.rendered .rendered_html {
    overflow-x: auto;
    overflow-y: hidden;
}

div.text_cell_render {
    /* font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif; */
    outline: none;
    resize: none;
    width: inherit;
    border-style: none;
    padding: 0.5em 0.5em 0.5em 0.4em;
    color: #000;
    box-sizing: border-box;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
}

/*
div.output_wrapper {

-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
color: #000;
font-size: 14px;
line-height: 20px;
box-sizing: border-box;
position: relative;
-webkit-box-orient: vertical;
-webkit-box-align: stretch;
display: flex;
flex-direction: column;
align-items: stretch;
z-index: 1; 
}
*/

div.output_wrapper {
    position: relative;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    z-index: 1;
}

/*
.output {

-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
color: #000;
font-size: 14px;
line-height: 20px;
box-sizing: border-box;
-webkit-box-orient: vertical;
-webkit-box-align: stretch;
display: flex;
flex-direction: column;
align-items: stretch;
}
*/

.output {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    display: flex;
    flex-direction: column;
    align-items: stretch;
}


/*
div.output_area {

-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
color: #000;
font-size: 14px;
line-height: 20px;
box-sizing: border-box;
padding: 0px;
page-break-inside: avoid;
-webkit-box-orient: horizontal;
-webkit-box-align: stretch;
display: flex;
flex-direction: row;
align-items: stretch;

}
*/

div.output_area {
    padding: 0px;
    page-break-inside: avoid;
    display: -webkit-box;
    -webkit-box-orient: horizontal;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: horizontal;
    -moz-box-align: stretch;
    display: box;
    box-orient: horizontal;
    box-align: stretch;
    display: flex;
    flex-direction: row;
    align-items: stretch;
}

div.output_subarea {
    overflow-x: auto;
    padding: 0.4em;
    -webkit-box-flex: 1;
    -moz-box-flex: 1;
    box-flex: 1;
    flex: 1;
    max-width: calc(100% - 14ex);
}

.rendered_html {
    color: #000;
}

div.section_header {
    text-align: center;
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
"""
  
  for section_schema in schema['widgets']:
        
    html+="""
<div tabindex="-1" id="notebook" class="border-box-sizing">
	<div class="container" id="notebook-container">    
    """
    
    html+=f"""
      <div class="section_header">
          <h1>{section_schema['title']}</h1>
      </div>
    """

    for widget_schema in section_schema['widgets']:
      
      if widget_schema['type']=='markdown':
                
        html+="""
		<div class="cell border-box-sizing text_cell rendered">
          <div class="prompt input_prompt">
			<div class="inner_cell">
				<div class="text_cell_render border-box-sizing rendered_html">
        """
        
        html+=convert_markdown(widget_schema['text'])
        
        html+="""
    			</div>
    		</div>
          </div>
		</div>        
        """
       
      elif widget_schema['type']=='chart':
        
        spec=charts[str(widget_schema['id'])]
        data_name=spec['data'].get('name', None)
        data_values=datasets.get(data_name, None)
        
        if data_name and data_values:
          print("move datasets to global var?")
          html+=gen_vega_vis_named_data(widget_schema['id'], spec, data_name, data_values)
          
        else: #not data_name and not data_values:
          html+=gen_vega_vis_no_named_data(widget_schema['id'], spec)
          
    html+="""
	</div>
</div>    
    """
        
  html+="""
</body>
</html> 
  """
  
  m=anvil.BlobMedia('text/html', html.encode(), name=report_row['title']+'.html')
  
  return m
  
  
      
def gen_vega_vis_named_data(div_id, spec, data_name, data_values):
  
  html=f"""
		<div class="cell border-box-sizing code_cell rendered">
			<div class="output_wrapper">
				<div class="output">
					<div class="output_area">
						<div class="output_html rendered_html output_subarea output_execute_result">

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

						</div>
					</div>			
				</div>
			</div>
		</div>  
  """

  return html


def gen_vega_vis_no_named_data(div_id, spec):
    
  html=f"""
		<div class="cell border-box-sizing code_cell rendered">
			<div class="output_wrapper">
				<div class="output">
					<div class="output_area">
						<div class="output_html rendered_html output_subarea output_execute_result">

							<div id=vis{div_id}></div>

							<script type="text/javascript">
							  var spec = {spec};
							  vegaEmbed('#vis{div_id}', spec, opts)

							</script>

						</div>
					</div>			
				</div>
			</div>
		</div>  
  """

  return html
  
 
  

  
  
  
  
  
  
  
  
  