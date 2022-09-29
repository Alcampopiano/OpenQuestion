from ._anvil_designer import dateTemplate


class date(dateTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

        self.tag.logic = None
        self.tag.logic_target_ids = []
        self.tag.current_value = None

    def date_picker_change(self, **event_args):
        self.tag.current_value = self.date_picker.date

        from .... import form

        for target_id in self.tag.logic_target_ids:
            form.check_logic_for_visibility(target_id)
