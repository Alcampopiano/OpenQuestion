from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

'https://RZCX3HWGWWPZJCOH.anvil.app/MLWEXSSLJT4I3SM3B4MURYXP'
'5bdbc005-055e-45ea-9a65-cd81529d59f5'

'https://RZCX3HWGWWPZJCOH.anvil.app/MLWEXSSLJT4I3SM3B4MURYXP#5bdbc005-055e-45ea-9a65-cd81529d59f5'

if not get_url_hash():
  
  # authentication here
  open_form('landing.select_form')
  
else:
    schema=anvil.server.call('get_form', get_url_hash())
    open_form('form.main', schema)
