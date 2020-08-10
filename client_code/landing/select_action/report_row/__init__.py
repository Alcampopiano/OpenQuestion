from ._anvil_designer import report_rowTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class report_row(report_rowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.label_title.text=self.item['title']
    self.link_build.tag.row=self.item

    # Any code you write here will run when the form opens.
  def link_build_report_click(self, **event_args):

    row=self.link_build.tag.row
    open_form('reports.main', row=row)