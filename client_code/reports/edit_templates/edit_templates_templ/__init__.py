from ._anvil_designer import edit_templates_templTemplate


class edit_templates_templ(edit_templates_templTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.image.source = self.item["images"].url

    def button_delete_click(self, **event_args):
        pass

    def form_show(self, **event_args):
        spec = self.item["templates"]
        self.json.set_json_editor(spec)
