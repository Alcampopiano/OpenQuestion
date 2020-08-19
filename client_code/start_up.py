from anvil import *
import anvil.microsoft.auth
import anvil.users
import anvil.server

if not get_url_hash():
  
  while not anvil.users.login_with_form():
    pass
  
  open_form('landing.main')
  
else:
    schema=anvil.server.call('get_form', get_url_hash())
    open_form('form.main', schema)
