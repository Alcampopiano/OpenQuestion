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
                            tag='selected_value',
                            **general_formats)
    
    type_drop_props=dict(items=['quantitaive', 'temporal', 
                                'nominal', 'ordinal'], 
                         tag='selected_value',
                         **general_formats)
    
    empty_text_props=dict(tag='text', **general_formats)
    
    field_drop_props=dict(items=['column_1', 'column_2'], tag='selected_value', **general_formats)
      
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
        
        
  def comps_to_spec(self, column_panel):

    spec={}
    for comp in column_panel.get_components():
      
      if comp.__name__ is 'node':
        key=comp.link_label.text
        res=self.comps_to_spec(comp.column_panel)
        spec.update({key: res})

        
        
      else:
        
        key=comp.label_prop.text
        prop_comp=comp.column_panel.get_components()[0]
        val=getattr(prop_comp, prop_comp.tag)
        spec.update({key: val})
        
    
    
    return spec


  def print_spec_click(self, **event_args):
    spec=self.comps_to_spec(self.column_panel)
    print(spec)

