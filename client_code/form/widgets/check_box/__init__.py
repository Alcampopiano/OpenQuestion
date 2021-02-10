from ._anvil_designer import check_boxTemplate
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
from .check_box_other import check_box_other

class check_box(check_boxTemplate):
  def __init__(self, options, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.tag.logic=None
    self.tag.options=options

    # Any code you write here will run when the form opens.
    for op in options['regular_options']:
      c=CheckBox(text=op, foreground='black')
      self.column_panel.add_component(c)
      
    if options['other_option']:
      check_other_form=check_box_other()
      check_other_form.text_box.placeholder=options['other_placeholder']
      check_other_form.check_box.text=options['other_option']
  
      self.column_panel.add_component(check_other_form)
      