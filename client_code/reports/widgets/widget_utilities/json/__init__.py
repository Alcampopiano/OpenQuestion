import json as json_lib

import anvil.http
import anvil
from anvil.js.window import JSONEditor

from ._anvil_designer import jsonTemplate


class json(jsonTemplate):
    def __init__(self, **properties):

        self.init_components(**properties)
        self.tag.form_shown = False

    def set_editor(self, spec):
        self.editor.set(spec)

    def get_editor_text_to_json(self):
        spec = self.editor.getText()
        spec = spec.replace("\n", "")
        spec = json_lib.loads(spec)

        return spec

    def on_editor_change(self):

        # print('soon anvil will allow proxy object to be sent to server')
        # print('no need then to use getText and deal with that as a string')
        spec = self.get_editor_text_to_json()
        self.tag.chart.tag.vl_spec = spec
        self.tag.chart.vega_embed()

    def form_show(self, **event_args):

        if not self.tag.form_shown:

            self.tag.form_shown = True

            spec = self.tag.chart.tag.vl_spec

            # schema=anvil.server.call('get_json_schema')

            # color-hex format not supported so changing it
            # and moving on with my life
            # schema['definitions']["HexColor"]['format']="uri"

            options = {
                "schema": anvil.get_open_form().tag.vl_schema,
                "mode": "code",
                "modes": ["code", "tree"],
                "onChange": self.on_editor_change,
            }

            container = anvil.js.get_dom_node(self)
            self.editor = JSONEditor(container, options, spec)
            # print(dir(self.editor))
