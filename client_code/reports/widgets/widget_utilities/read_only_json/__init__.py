import anvil
import anvil.http
from anvil.js.window import JSONEditor

from ._anvil_designer import read_only_jsonTemplate


class read_only_json(read_only_jsonTemplate):
    def __init__(self, **properties):

        self.init_components(**properties)

    def set_json_editor(self, spec, **event_args):

        options = {
            # 'schema': anvil.get_open_form().tag.vl_schema,
            "mode": "code",
            "modes": ["code", "view"],
        }

        container = anvil.js.get_dom_node(self)
        self.editor = JSONEditor(container, options, spec)
