from anvil import *

# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

if get_url_hash():
  open_form('form.main')
  
else:
  open_form('build.main')