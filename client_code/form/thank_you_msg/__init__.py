from ._anvil_designer import thank_you_msgTemplate


class thank_you_msg(thank_you_msgTemplate):
    def __init__(self, thank_you_msg, **properties):
        self.init_components(**properties)

        self.custom_html.html = thank_you_msg
