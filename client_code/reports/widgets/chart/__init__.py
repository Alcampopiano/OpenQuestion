from ._anvil_designer import chartTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..chart_utilities.node import node
from ..chart_utilities.properties import properties

class chart(chartTemplate):
  def __init__(self, section, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    #self.chart_display.vl_spec = anvil.server.call('make_chart')
    
    from ..toolbar import toolbar
    toolbar=toolbar(align='left', section=section, parent=self)
    
    self.add_component(toolbar)
    
    general_formats=dict(
    font_size=14,
    spacing_above=None,
    spacing_below=None)
    
    mark_drop_props=dict(items=['bar', 'area', 'line', 'rect',
                           'circle', 'text', 'tick', 'rule'],
                            **general_formats)
    
    type_drop_props=dict(items=['quantitaive', 'temporal', 
                              'nominal', 'ordinal'], **general_formats)
    
    empty_text_props=dict(**general_formats)
    
    field_drop_props=dict(items=['column_1', 'column_2'], **general_formats)
      
    spec={
  "config": {
    "view": {
      "continuousWidth": TextBox(**empty_text_props), "continuousHeight": TextBox(**empty_text_props)}
  },
  "mark": DropDown(**mark_drop_props),
  "encoding": {
    "x": {"type": DropDown(**type_drop_props), "field": DropDown(**field_drop_props)},
    "y": {"type": DropDown(**type_drop_props), "field": DropDown(**field_drop_props)}
    },
  }
    
    self.spec_to_comps(spec, parent=self)
    
    
  def spec_to_comps(self, spec, parent=None, **event_args):
    
    for k in spec:
      
      if type(spec[k]) is dict:
        
        dict_node=node(node_text=k)
        parent.column_panel.add_component(dict_node)
        
        self.spec_to_comps(spec[k], parent=dict_node)
        
      else:
        
        prop=properties(prop_text=k, spec_comp=spec[k])
        parent.column_panel.add_component(prop)

  def print_spec_click(self, **event_args):

    spec=self.comps_to_spec()

