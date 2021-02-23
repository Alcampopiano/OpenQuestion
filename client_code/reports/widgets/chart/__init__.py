from ._anvil_designer import chartTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..widget_utilities.json import json
from ..widget_utilities.vega_lite import vega_lite
from ..widget_utilities.gen_chart_params import gen_chart_params

class chart(chartTemplate):
  def __init__(self, section, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    from ..toolbar import toolbar
    toolbar=toolbar(align='left', section=section, parent=self)
    self.add_component(toolbar)
    
    json_editor=json()
    chart=vega_lite()
    self.tag.chart=chart
    self.tag.json_editor=json_editor
     
    json_editor.tag.parent=self.column_panel_json_container
    json_editor.tag.chart=chart

    self.column_panel_json_container.add_component(json_editor, full_width_row=True)
    self.column_panel_vis_container.add_component(chart, full_width_row=True)
    

  def button_nav_click(self, **event_args):
    
    chart_schemas=self.tag.auto_charts
    ind=self.tag.current_auto_chart_ind
          
    if not ind==len(chart_schemas)-1 and event_args['sender'].icon=='fa:arrow-circle-right':
        spec=chart_schemas[ind+1]
        self.tag.json_editor.set_editor(spec)
        self.tag.json_editor.on_editor_change()        
        self.tag.current_auto_chart_ind+=1
      
    elif not ind==0 and event_args['sender'].icon=='fa:arrow-circle-left':
        spec=chart_schemas[ind-1]
        self.tag.json_editor.set_editor(spec)
        self.tag.json_editor.on_editor_change()
        self.tag.current_auto_chart_ind-=1
      

  def button_generate_click(self, **event_args):
    
    chart_params=gen_chart_params()
    c=confirm(chart_params,
              buttons=[('ok', 'ok'), ('cancel', 'cancel')],
              large=True,title='Choose parameters for automatic chart creation')

    if c=='ok' and chart_params.flow_panel_columns.tag.current_cols:
        
      cols=chart_params.flow_panel_columns.tag.current_cols
      dataset_name=chart_params.drop_down_dataset.selected_value
      survey_row=get_open_form().tag.row
      chart_schemas=anvil.server.call('data_to_spec', survey_row, cols, dataset_name)
      self.build_auto_charts(chart_schemas)
      
    
  def build_auto_charts(self, chart_schemas, **event_args):
    
    if chart_schemas:
      self.tag.auto_charts=chart_schemas
      self.button_right.visible=True
      self.button_left.visible=True
      spec=chart_schemas[0]
      self.tag.json_editor.set_editor(spec)
      self.tag.json_editor.on_editor_change()
      self.tag.current_auto_chart_ind=0
      
    else:
      self.button_right.visible=False
      self.button_left.visible=False
      alert('Please see the docs on automatic chart generation', 
            title='No charts could be generated given the templates and chosen parameters')
      
    
  def button_save_template_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
    
    #self.column_panel.add_component(json_chart, full_width_row=True)
    #self.tag.chart_wigets.append(chart)
    
#   def spec_to_comps(self, spec, parent=None, **event_args):
    
#     for k in spec:
      
#       if type(spec[k]) is dict:
        
#         dict_node=node(node_text=k)
#         parent.column_panel.add_component(dict_node)
        
#         self.spec_to_comps(spec[k], parent=dict_node)
        
#       else:
        
#         prop=properties(prop_text=k, spec_comp=spec[k])
#         parent.column_panel.add_component(prop)
#         self.tag.comp_list.append(prop)
        
        
#   def comps_to_spec(self, column_panel):

#     spec={}
#     for comp in column_panel.get_components():
      
#       if comp.__name__ is 'node':
#         key=comp.link_label.text
#         res=self.comps_to_spec(comp.column_panel)
#         spec.update({key: res})

#       else:
        
#         key=comp.label_prop.text
#         prop_comp=comp.column_panel.get_components()[0]
#         val=getattr(prop_comp, prop_comp.tag)
#         spec.update({key: val})
        
#     return spec
    
    







