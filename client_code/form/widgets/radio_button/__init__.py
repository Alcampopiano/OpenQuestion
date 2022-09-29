import anvil

from ._anvil_designer import radio_buttonTemplate


class radio_button(radio_buttonTemplate):
    def __init__(self, options, group_name, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.tag.logic = None
        self.tag.logic_target_ids = []
        self.tag.current_value = None

        # Any code you write here will run when the form opens.
        for op in options:
            b = anvil.RadioButton(text=op, foreground="black")
            b.group_name = group_name
            b.set_event_handler("clicked", self.radio_clicked)
            self.column_panel.add_component(b)

    def radio_clicked(self, **event_args):
        self.tag.current_value = event_args["sender"].text

        from .... import form

        for target_id in self.tag.logic_target_ids:
            form.check_logic_for_visibility(target_id)
