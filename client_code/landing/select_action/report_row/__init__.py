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
    self.button_build.tag.row=self.item

    # Any code you write here will run when the form opens.
  def button_build_click(self, **event_args):

    print(' this context manager is not working for some reason')
    with Notification('', title='please wait...'):
      row=self.button_build.tag.row
      open_form('reports.main', row=row)

  def download_click(self, **event_args):
    Notification('should download the html report', 
                 title="not yet implemented").show()





