import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.microsoft.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a package.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .reports.widgets import Package1
#
#    Package1.say_hello()
#

def say_hello():
  print("Hello, world")
