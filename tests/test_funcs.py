import os
import threading
import time
from server_code.server_surveys import *
import anvil.server
import pytest
import uuid
from datetime import datetime

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

# id
form_id = str(uuid.uuid4())

@pytest.fixture(scope="session", autouse=True)
def set_up_and_tear_down():

  """
  Everything before "yield" is run before any tests
  Everything after "yield" is run after all tests have finished
  """

  # kill process on port in case it is running
  os.system("fuser -k 3030/tcp")

  # func to call app server
  def start_server():
    os.system("anvil-app-server --app ../OpenQuestion --uplink-key 42 --port 3030")

  # start app server on a thread, allowing the rest of the script to run
  threading.Thread(target=start_server).start()

  # give time for the web server to spin up before continuing
  time.sleep(60)

  # connect
  anvil.server.connect('42', url="ws://localhost:3030/_/uplink")

  # add a survey
  app_tables.forms.add_row(form_id=form_id, last_modified=datetime.now(),
                           schema=schema, title=schema['title'])

  yield True

  # disconnect from uplink
  anvil.server.disconnect()

  # kill process on that port
  os.system("fuser -k 3030/tcp")

def test_delete_survey():

  # current number of surveys
  init_num_forms = len(app_tables.forms.search())

  # add a survey to the database
  delete_survey(form_id)

  # a simple assertion that there is one more survey in the database
  assert init_num_forms > len(app_tables.forms.search())

def test_save_schema():

  # current number of surveys
  init_num_forms=len(app_tables.forms.search())

  # add a survey to the database
  save_schema(None, schema)

  # a simple assertion that there is one more survey in the database
  assert init_num_forms < len(app_tables.forms.search())

def test_save_survey_settings():

  row=app_tables.forms.add_row(form_id=form_id, schema=schema,
                           title=schema['title'])

  settings_in_schema={'survey_color': '#F0F0F0',
                   'thank_you_msg': '#Thank you!'}

  settings_in_datatable={'opening_date': None,
                         'closing_date': None}

  save_survey_settings(form_id, settings_in_schema, settings_in_datatable)

  assert schema['settings'] != row['schema']['settings']