from ._anvil_designer import copy_linkTemplate


class copy_link(copy_linkTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def copy_click(self, text_to_copy, **event_args):

        self.call_js("copyclip", text_to_copy)
        # self.label_1.visible=True
