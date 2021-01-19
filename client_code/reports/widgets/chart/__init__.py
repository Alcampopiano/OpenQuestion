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
     
    json_editor.tag.parent=self.column_panel_json_container
    json_editor.tag.chart=chart

    self.column_panel_json_container.add_component(json_editor, full_width_row=True)
    self.column_panel_vis_container.add_component(chart, full_width_row=True)

    
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
    
    



