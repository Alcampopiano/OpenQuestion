from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
import anvil.server


if not get_url_hash():
  
  while not anvil.users.login_with_form():
    pass
  
  # disabling report module
  # open_form('landing.main')
  open_form('landing.select_action_survey')
  
else:
    schema=anvil.server.call('get_form', get_url_hash())
    open_form('form.main', schema)
