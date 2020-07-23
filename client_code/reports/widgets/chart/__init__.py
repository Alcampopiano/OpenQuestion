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
    
    from ..toolbar import toolbar
    toolbar=toolbar(align='left', section=section, parent=self)
    self.add_component(toolbar)
    
    # can a dict be used for easy look up?
    self.tag.comp_list=[]
    
    # formatting for components that represent editable aspects of the VL spec
    general_formats=dict(
    font_size=14,
    spacing_above=None,
    spacing_below=None)
    
    mark_drop_props=dict(items=['bar', 'area', 'line', 'rect',
                                'circle', 'text', 'tick', 'rule'],
                            tag='selected_value',
                            **general_formats)
    
    agg_drop_props=dict(items=['', 'count', 'sum', 'mean', 'var'],
                            tag='selected_value',
                            **general_formats)
    
    type_drop_props=dict(items=['quantitative', 'temporal', 
                                'nominal', 'ordinal'], 
                         tag='selected_value',
                         **general_formats)
    
    empty_text_props=dict(tag='text', text=300, type='number', **general_formats)
    
    field_drop_props=dict(tag='selected_value', **general_formats)
    
    bin_check_props=dict(tag='checked', **general_formats)
      
    # VL spec template
    spec={
  "config": {
    "view": {
      "continuousWidth": TextBox(**empty_text_props), "continuousHeight": TextBox(**empty_text_props)}
     },
  "mark": DropDown(**mark_drop_props),
  "encoding": {
    "x": {"type": DropDown(**type_drop_props), "field": DropDown(**field_drop_props), "bin": CheckBox(**bin_check_props), "aggregate": DropDown(**agg_drop_props)},
    "y": {"type": DropDown(**type_drop_props), "field": DropDown(**field_drop_props), "bin": CheckBox(**bin_check_props), "aggregate": DropDown(**agg_drop_props)},
    "color": {"type": DropDown(**type_drop_props), "field": DropDown(**field_drop_props)},
    "column": {"type": DropDown(**type_drop_props), "field": DropDown(**field_drop_props)}
    },
   }
    
    self.tag.spec=spec
    
    
  def spec_to_comps(self, spec, parent=None, **event_args):
    
    for k in spec:
      
      if type(spec[k]) is dict:
        
        dict_node=node(node_text=k)
        parent.column_panel.add_component(dict_node)
        
        self.spec_to_comps(spec[k], parent=dict_node)
        
      else:
        
        prop=properties(prop_text=k, spec_comp=spec[k])
        parent.column_panel.add_component(prop)
        self.tag.comp_list.append(prop)
        
        
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


  def render_spec_click(self, **event_args):
    spec=self.comps_to_spec(self.column_panel)
    dataset=self.tag.dataset
    spec=anvil.server.call('make_chart', spec, dataset)
    self.chart_display.vl_spec = spec
    self.column_panel_vl_container.visible=True

  def upload_change(self, file, **event_args):
    
    if file:
      columns=anvil.server.call('get_columns', file)
      self.tag.dataset=file
      self.file_loader.text=file.name

    # set the spec?
    spec=self.tag.spec
    self.spec_to_comps(spec, parent=self)

    # set dropdown items to columns
    for c in self.tag.comp_list:
      if c.label_prop.text=='field':
        c.column_panel.get_components()[0].items=['']+ columns
        
    #self.button_render.visible=True
    self.column_panel_container.visible=True
    
    



