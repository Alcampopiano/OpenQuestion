import os
import threading
import time
from server_code.server_surveys import *
# import anvil.server
# import anvil.users
# from tables import app_tables
# import uuid

# look at what's running on a port
# lsof -i :3030

# kill process on port in case it is running
os.system("fuser -k 3030/tcp")

def start_server():
  os.system("anvil-app-server --app ../OpenQuestion --uplink-key 42")

threading.Thread(target=start_server).start()
time.sleep(10)

anvil.server.connect('42', url="ws://localhost:3030/_/uplink")
u = app_tables.users.get(email='test@test.com')

if not u:
  u=app_tables.users.add_row(email='test@test.com')

# basic survey
schema={
  "title": "simple survey",
  "settings": {
  "survey_color": "#2196F3",
  "thank_you_msg": "#Thank you!"
  },
  "num_widgets": 2,
  "widgets": [
    {
      "id": 0,
      "type": "section",
      "logic": None,
      "title": "section",
      "widgets": [
        {
          "id": 1,
          "type": "text_box",
          "logic": None,
          "title": "what's your name?",
          "number": False,
          "mandatory": True,
          "placeholder": "placeholder here"
        }
      ]
    }
  ]
}

def test_save_schema():
  cur_num_forms=len(app_tables.forms.search())
  save_schema(None, schema)
  assert cur_num_forms < len(app_tables.forms.search())
