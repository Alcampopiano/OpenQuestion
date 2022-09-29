import anvil

from ....utilities import augment
from ._anvil_designer import sectionTemplate


class section(sectionTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

        self.tag.logic = None
        self.role = "section_shadow"
        augment.set_event_handler(self, "click", self.section_select)

    def form_show(self, **event_args):
        # anvil.get_open_form().tag.active_section=self
        self.section_border_toggle()

    def section_border_toggle(self, **event_args):

        sections = anvil.get_open_form().column_panel.get_components()

        for section in sections:
            if section is not self:
                section.role = "section_no_shadow"

    def section_select(self, **event_args):

        if self.role == "section_no_shadow":
            self.role = "section_shadow"
            # anvil.get_open_form().tag.active_section=self
            self.section_border_toggle()
