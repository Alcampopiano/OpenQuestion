import os
import threading
import time
from server_code.server_surveys import *
import anvil.server
import pytest
import uuid
from datetime import datetime
import pandas as pd
import io

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

  yield True

  # disconnect from uplink
  anvil.server.disconnect()

  # kill process on that port
  os.system("fuser -k 3030/tcp")

def test_delete_survey():

  form_id=str(uuid.uuid4())

  # add a survey
  app_tables.forms.add_row(form_id=form_id, last_modified=datetime.now(),
                           schema=schema, title=schema['title'])

  # current number of surveys
  init_num_forms = len(app_tables.forms.search())

  # add a survey to the database
  delete_survey(form_id)

  # a simple assertion that there is one more survey in the database
  assert init_num_forms > len(app_tables.forms.search())

def test_submit_data():

  """
  Test that data is stored into the data after a submission

  Test that columns are added to the dataframe as expected even when
  using query string parameters in the URL hash
  """

  form_id=str(uuid.uuid4())

  # add a survey
  app_tables.forms.add_row(form_id=form_id, last_modified=datetime.now(),
                           schema=schema, title=schema['title'])

  # submit some initial data
  cols=['a', 'b', 'c']

  data=[1,2,3]
  submit_data(cols.copy(), data.copy(), {'form_id': form_id})

  # submit data with query parameters (meta data)
  cols_from_hash=['form_id', '1st_param', '2nd_param']
  submit_data(cols.copy(), data.copy(), {cols_from_hash[0]: form_id,
                           cols_from_hash[1]: 'foo',
                           cols_from_hash[2]: 'bar'})

  media=app_tables.forms.get(form_id=form_id)['submissions']
  df = pd.read_csv(io.BytesIO(media.get_bytes()), index_col=0)
  should_be_cols=cols + cols_from_hash
  new_cols=list(df.columns)

  assert new_cols==should_be_cols

def test_check_opening_closing_dates():

  """
  assert that a survey is deemed inactive if closing date has passed
  """

  x = datetime(2017, 11, 16, 23, 45, 15, 0, anvil.tz.tzoffset(hours=3))
  y = datetime(2018, 11, 16, 23, 45, 15, 0, anvil.tz.tzoffset(hours=3))

  try:
    check_opening_closing_dates(x, y)
  except Exception as e:
    error_str=str(e)

  assert error_str == 'survey inactive'

def test_get_form():

  form_id=str(uuid.uuid4())

  # add a survey
  app_tables.forms.add_row(form_id=form_id, last_modified=datetime.now(),
                           schema=schema, title=schema['title'])

  the_schema=get_form({'form_id': form_id, 'preview': True})

  assert the_schema==schema

def test_save_schema():

  # current number of surveys
  init_num_forms=len(app_tables.forms.search())

  # add a survey to the database
  save_schema(None, schema)

  # a simple assertion that there is one more survey in the database
  assert init_num_forms < len(app_tables.forms.search())

def test_save_survey_settings():

  form_id=str(uuid.uuid4())

  # add a survey
  row=app_tables.forms.add_row(form_id=form_id, last_modified=datetime.now(),
                           schema=schema, title=schema['title'])

  settings_in_schema={'survey_color': '#F0F0F0',
                   'thank_you_msg': '#Thank you!'}

  settings_in_datatable={'opening_date': None,
                         'closing_date': None}

  save_survey_settings(form_id, settings_in_schema, settings_in_datatable)

  assert schema['settings'] != row['schema']['settings']

