from ._anvil_designer import thank_you_msgTemplate


class thank_you_msg(thank_you_msgTemplate):
    def __init__(self, thank_you_msg, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.
        self.custom_html.html = thank_you_msg
