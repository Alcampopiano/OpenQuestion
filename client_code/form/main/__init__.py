from ._anvil_designer import mainTemplate
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
from ... import form
from ...landing.settings import ColorChanger

class main(mainTemplate):
  def __init__(self, schema, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.survey_color_change(schema['settings']['survey_color'])
    
    submit_button=Button(text='submit', role='primary-color')
    submit_button.set_event_handler('click', self.submit_click)
    self.add_component(submit_button)
    self.label_title.text=schema['title']
    form.build_form(schema, self.column_panel)  
    
  def submit_click(self, **event_args):
    form.submit_data(self.column_panel)
    
    
  def form_show(self, **event_args):
    self.color_rows()
    self.column_panel.get_components()[0].section_select()
    
    
  def color_rows(self, **event_args):
    
    for section in self.column_panel.get_components():
            
      for i, comp in enumerate(section.column_panel.get_components()):
  
        if not i%2:
          comp.background='theme:Gray 100'
          
        else:
          comp.background='white'
        
  def hide_last_hr(self, **event_args):
    
    for section in self.column_panel.get_components():
      
      found=False
      for comp in reversed(section.column_panel.get_components()):
        
        if comp.visible and not found:
          comp.hr.visible=False
          found=True
          
        else:
          comp.hr.visible=True
          
          
  def survey_color_change(self, color, **event_args):
    
    if color:
      
      # darken hex to get a second primary color
      color_darker=self.darken_hex(.1, color)
      
      ColorChanger.set_theme({'Primary 500': color,
                              'Primary 700': color_darker,
                              #'Secondary 500': color,
                              #'Secondary 700': color_darker
                              })
          
  def darken_hex(self, perc, color):
      
      red, green, blue=self.hex_to_rgb(color)
      
      red=round(red-(perc*red))
      green=round(green-(perc*green))
      blue=round(blue-(perc*blue))
      
      return '#%02x%02x%02x' % (red, green, blue)
    
  def hex_to_rgb(self, value):
      value = value.lstrip('#')
      lv = len(value)
      if lv == 1:
          v = int(value, 16)*17
          return v, v, v
      if lv == 3:
          return tuple(int(value[i:i+1], 16)*17 for i in range(0, 3))
        
      return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))
 
