# Advanced usage
OpenQuestion's GUI can handle standard survey development and therefore this section is
only intended for more advanced use cases. Where noted, certain topics are relevent only to
OpenQuestion's administrator(s).

## Accessing the Python Shell (for administrators)
From the command line (where the OpenQuestion is below the current directory) run the app server 
with the `--shell` option. This will drop you into a Python interpreter that has access to
OpenQuestion's priviledged code and database. 

```
anvil-app-server --app OpenQuestion --shell
```

## Accessing the Python Shell (for survey developers)
Developers can also interact with OpenQuestion's server code and databases from Python.
The administrator must first generate 
a token (a so-called [Uplink](https://anvil.works/docs/uplink) key) and associate it with 
OpenQuestion as follows:

```
 anvil-app-server --app OpenQuestion --uplink-key <you-secret-key>
```

!!! danger "Admins, be careful when creating an Uplink key"
    Uplink keys should be long, secure, and random. Do not share the key
    with anyone except for those who you want to have access to
    OpenQuestion's privileged server code and databases

Developers can now connect to OpenQuestion with Python code by following these steps:

```
pip install anvil-uplink
```

```python
import anvil.server

# connecting to OpenQuestion
anvil.server.connect("[uplink-key goes here]", url="ws://your-runtime-server:3030/_/uplink")`
```

Once sucessfully connected, developers will have priviledged access to OpenQuestion's server code
and databases from their Python environment.

## JSON representation of surveys
OpenQuestion represents surveys as a Python dictionary (stored as a JSON object in the backend database). The following
two examples show the `dict` representation of two surveys: one that is simple, followed by one that is more complex.
By studying these structures, one can learn how to create and modify surveys programatically 
(also, see the sections pertaining to working with the Surveys table). 

In general, the survey `dict` is a nested, somewhat self-similar structure. For example,

- The survey itself contains sections (a type of widget)
- Sections contain the typical UI widgets (e.g., text_box, drop_down, etc)
- The UI widgets contain all of the properties set in the survey designer 
(title, placeholder, mandatory flag, branching logic, etc)

??? example "Simple survey (click)"
    ```python
    my_survey={
    "title": "simple survey",
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
    ],
    "num_widgets": 2
    }
    ```
    
??? example "A more complex survey (click)"
    ```python
    {
    "title": "science survey",
    "widgets": [
    {
      "id": 0,
      "type": "section",
      "logic": None,
      "title": "About you",
      "widgets": [
        {
          "id": 1,
          "text": "This is a survey about **you** and **science**.\n\nFor more information about science click [here](https://en.wikipedia.org/wiki/Science).\n\n- these \n- are \n- bullets\n\nThis is scientifically proven to be the cutest image:\n\n<img src=\"https://i.imgur.com/gPb2phg.gif\" width=\"191\" height=\"200\">\n\n",
          "type": "markdown",
          "logic": None,
          "title": "",
          "placeholder": "markdown supported"
        },
        {
          "id": 2,
          "type": "text_box",
          "logic": None,
          "title": "What is your name?",
          "number": False,
          "mandatory": False,
          "placeholder": "name goes here"
        },
        {
          "id": 7,
          "type": "date",
          "logic": None,
          "title": "What is your date of birth?",
          "format": "%Y-%m-%d",
          "mandatory": False,
          "placeholder": "date goes here"
        },
        {
          "id": 3,
          "type": "text_area",
          "logic": None,
          "title": "Tell me about yourself",
          "placeholder": "text goes here"
        },
        {
          "id": 4,
          "type": "drop_down",
          "logic": None,
          "title": "What is your highest completed educational level?",
          "options": "high school diploma\ncollege diploma or university degree\nI have do not have a high school diploma",
          "mandatory": True,
          "placeholder": "select from here"
        },
        {
          "id": 11,
          "type": "radio_button",
          "logic": None,
          "title": "Are you interested in science?",
          "options": "Yes\nNo"
        }
      ]
    },
    {
      "id": 5,
      "type": "section",
      "logic": None,
      "title": "About you and science",
      "widgets": [
        {
          "id": 8,
          "type": "check_box",
          "logic": None,
          "title": "Which scientific topics are you interested in? (check all that apply)",
          "options": "mathematics\ngeography\ndata science\nstatistics\nphysics\nneuroscience"
        },
        {
          "labels": "not satisfied\nmeh\nvery satisfied",
          "min_val": "0",
          "value": "50",
          "type": "slider",
          "title": "How satisfied were you with your last science course? ",
          "id": 10,
          "logic": None,
          "step": "1",
          "max_val": "100"
        },
        {
          "id": 12,
          "type": "text_area",
          "logic": {
            "func": "any",
            "conditions": [
              {
                "id": 10,
                "title": "How satisfied were you with your last science course? ",
                "value": 40,
                "comparison": "<"
              }
            ]
          },
          "title": "In your opinion, what would improve science education?",
          "placeholder": "Explain here"
        }
      ]
    }
    ],
    "num_widgets": 22
    }
    ```

## Using the Surveys table from Python code
The Surveys table contains all surveys that are created in OpenQuestion.

!!! note "Interacting with tables"
    For more information on the the API used for interacting with tables, 
    please see Anvil's [DataTables documentation](https://anvil.works/docs/data-tables/data-tables-in-code).
    
The Surveys table has the following columns:

- _survey_id_: A long, random, secure, and unique string
- _title_: The survey title
- _last_modified_: A Python datetime object
- _schema_: A JSON representation of the survey's structure (does not contain submission data)
- _submissions_: A CSV [media object](https://anvil.works/docs/media) which accumulates submissions
- _opening_date_: A Python datetime object for an opening date
- _closing_date_: A Python datetime object for an closing date
- _thank_you_msg_: A string of Markdown text for the thank you message

### Adding a survey
The following example demonstrates how to programatically add a survey to the Surveys table.

```python
from anvil.tables import app_tables

my_survey={
  "title": "simple survey",
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
  ],
  "num_widgets": 2
}

app_tables.surveys.add_row(
    survey_id='you secure survey ID', # A long, random, secure, and unique string
    title='simple survey', 
    schema=my_survey, # A Python dictionary following OpenQuestion's expected format
    submissions=None,
    opening_date=None,
    closing_date=None,
    thank_you_msg='# Thank you!') # Markdown goes here
```

### Deleting a survey
The following example demonstrates how to programatically delete a survey from the Surveys table.

```python
from anvil.tables import app_tables

# Searching based on title property but any other search parameter can be used. 
# See Anvil's Datatable documentation https://anvil.works/docs/data-tables/data-tables-in-code
row=app_tables.surveys.get(title='simple survey')
row.delete()
```

### Modifying a survey
The following example demonstrates how to programatically modify a survey from the Surveys table.

```python
from anvil.tables import app_tables

row=app_tables.surveys.get(title='simple survey')

# modifying the survey's title
row['title']='My new title'
```

## Using the Users table from Python
OpenQuestion stores user information in the Users table.

### adding a user

### deleting a user

### password reset


## URL parameters