from ._anvil_designer import drop_downTemplate


class drop_down(drop_downTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

        self.tag.logic = None
        self.tag.logic_target_ids = []
        self.tag.current_value = None

    def drop_down_change(self, **event_args):
        self.tag.current_value = self.drop_down.selected_value

        from .... import form

        for target_id in self.tag.logic_target_ids:
            form.check_logic_for_visibility(target_id)
