from ._anvil_designer import select_form_rowTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class select_form_row(select_form_rowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_title.text=self.item['title']
    self.link_build.tag.row=self.item

  def link_build_click(self, **event_args):
    """This method is called when the link is clicked"""
    
    row=self.link_build.tag.row
    open_form('build.main', row=row)

  def data_click(self, **event_args):
    """This method is called when the link is clicked"""
    row=self.link_build.tag.row
    download(row['submissions'])


  