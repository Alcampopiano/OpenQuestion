import anvil.server
import anvil

from ._anvil_designer import gen_chart_paramsTemplate


class gen_chart_params(gen_chart_paramsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.flow_panel_columns.tag.current_cols = []

    def form_show(self, **event_args):
        data_dicts = anvil.get_open_form().tag.data_dicts
        names = [k for k in data_dicts]
        self.drop_down_dataset.items = names
        self.set_columns()

    def set_columns(self, **event_args):
        name = self.drop_down_dataset.selected_value
        data_dicts = anvil.get_open_form().tag.data_dicts
        cols = data_dicts[name][0].keys()
        self.drop_down_columns.items = cols
        self.flow_panel_columns.tag.current_cols = []
        [c.remove_from_parent() for c in self.flow_panel_columns.get_components()]

    def drop_down_dataset_change(self, **event_args):
        """This method is called when an item is selected"""
        self.set_columns()

    def drop_down_columns_change(self, **event_args):
        """This method is called when an item is selected"""
        value = self.drop_down_columns.selected_value

        if value and value not in self.flow_panel_columns.tag.current_cols:
            b = anvil.Button(
                text=value, role="primary-color", font_size=12, icon="fa:times-circle"
            )
            b.set_event_handler("click", self.but_click)
            self.flow_panel_columns.add_component(b)
            self.flow_panel_columns.tag.current_cols.append(value)

    def but_click(self, **event_args):
        self.flow_panel_columns.tag.current_cols.remove(event_args["sender"].text)
        event_args["sender"].remove_from_parent()
