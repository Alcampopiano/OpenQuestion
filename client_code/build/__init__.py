import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import *
from .. import widgets

def build_form(schema, column_panel):
  
  column_panel.tag.title=schema['title']
  column_panel.tag.id=schema['id']
  #print(schema)
  
  for section_schema in schema['widgets']:
    
    section=widgets.section()
    section.text_box_title.text=section_schema['title']
    section.tag.id=section_schema
    section.tag.logic=section_schema['logic']
    
    for widget_schema in section_schema['widgets']:
      
      if widget_schema['type']=='text_box':
        
        widget=widgets.text_box(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.text_box_placeholder.placeholder=widget_schema['placeholder']
        
      elif widget_schema['type']=='drop_down':
        widget=widgets.drop_down(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.text_area_options.text=widget_schema['options']
        widget.text_box_placeholder.placeholder=widget_schema['placeholder']
        
      elif widget_schema['type']=='date':
        widget=widgets.date(section=section)
        widget.text_box_title.text=widget_schema['title']
        widget.text_box_format.text=widget_schema['format']
        widget.text_box_placeholder.placeholder=widget_schema['placeholder']

      # remove this once all components are accounted for
      if widget_schema['type'] in ('text_box', 'drop_down', 'date'):
        widget.tag.logic=widget_schema['logic']
        widget.tag.id=widget_schema['id']
        section.column_panel.add_component(widget)

    
    column_panel.add_component(section)
    
    
def build_schema(column_panel):
  
  schema={}
  schema['title']=column_panel.text_box_title.text
  schema['id']=column_panel.tag.id
  schema['widgets']=[]

  for section in column_panel.get_components():
    
#     {'title': 'section_1',
#  'id': 1,
#  'type': 'section',
#  'visible': True,
#  'logic': None,
#  'widgets': [{'title': 'widget_1',
#    'id': 2,
#    'type': 'text_box',
#    'placeholder': 'place',
#    'visible': True,
#    'text': 'hello',
#    'logic': None},
#   {'title': 'widget_2',
#    'id': 3,
#    'type': 'drop_down',
#    'placeholder': 'place',
#    'options': [1, 2, 3, 4, 5, 6, 7],
#    'visible': True,
#    'logic': [{'id': 4,
#      'func': 'all',
#      'visible': False,
#      'conditions': [{'comparison': '>', 'value': 3},
#       {'comparison': '<=', 'value': 6}]},
#     {'id': 6,
#      'func': 'any',
#      'visible': True,
#      'conditions': [{'comparison': '>', 'value': 3}]}]},
#   {'title': 'widget_3',
#    'id': 4,
#    'type': 'text_box',
#    'placeholder': 'place',
#    'visible': True,
#    'text': 'hello2',
#    'logic': None}]}
    
    section_schema={}
    section_schema['type']='section'
    section_schema['title']=section.text_box_title.text
    section_schema['id']=1
    section_schema['visible']=True # should be a tag property
    section_schema['logic']=None # should be a tag property
    section_schema['widgets']=[]
    
    for widget in section.column_panel.get_components():
      
      widget_schema={}
      print(type(widget))
      
      if 'text_box' in str(type(widget)):
        
        widget_schema['type']='text_box'
        widget_schema['title']=widget.text_box_title.text
        widget_schema['id']=1
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        widget_schema['placeholder']=widget.text_box_placeholder.text
    
      elif 'drop_down' in str(type(widget)):
        
        widget_schema['type']='drop_down'
        widget_schema['title']=widget.text_box_title.text
        widget_schema['id']=1
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        widget_schema['placeholder']=widget.text_box_placeholder.text
        widget_schema['options']=widget.text_area_options.text
     
      elif 'date' in str(type(widget)):
        
        widget_schema['type']='date'
        widget_schema['title']=widget.text_box_title.text
        widget_schema['id']=1
        widget_schema['visible']=True  # should be a tag property
        widget_schema['logic']=None # should be a tag property
        widget_schema['placeholder']=widget.text_box_placeholder.text
        widget_schema['format']=widget.text_box_format.text
    
    
      section_schema['widgets'].append(widget_schema)
      
    schema['widgets'].append(section_schema)
    
  print(schema)

  return schema
 

