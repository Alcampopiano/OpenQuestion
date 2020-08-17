from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime


if not get_url_hash():
  
  # authentication here
  open_form('landing.select_action')
  
else:
    schema=anvil.server.call('get_form', get_url_hash(), datetime.now())
    open_form('form.main', schema)
