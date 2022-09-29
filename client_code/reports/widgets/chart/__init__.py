import anvil
import anvil.server

from ..widget_utilities.gen_chart_params import gen_chart_params
from ..widget_utilities.json import json
from ..widget_utilities.vega_lite import vega_lite
from ._anvil_designer import chartTemplate

# from anvil.js.window import vega


class chart(chartTemplate):
    def __init__(self, section, **properties):
        self.init_components(**properties)

        from ..toolbar import toolbar

        toolbar = toolbar(align="left", section=section, parent=self)
        self.add_component(toolbar)

        json_editor = json()
        chart = vega_lite()
        self.tag.chart = chart
        self.tag.json_editor = json_editor

        json_editor.tag.parent = self.column_panel_json_container
        json_editor.tag.chart = chart

        self.column_panel_json_container.add_component(json_editor, full_width_row=True)
        self.column_panel_vis_container.add_component(chart, full_width_row=True)

    def button_nav_click(self, **event_args):

        chart_schemas = self.tag.auto_charts
        ind = self.tag.current_auto_chart_ind

        if (
            not ind == len(chart_schemas) - 1
            and event_args["sender"].icon == "fa:arrow-circle-right"
        ):
            spec = chart_schemas[ind + 1]
            self.tag.json_editor.set_editor(spec)
            self.tag.json_editor.on_editor_change()
            self.tag.current_auto_chart_ind += 1

        elif not ind == 0 and event_args["sender"].icon == "fa:arrow-circle-left":
            spec = chart_schemas[ind - 1]
            self.tag.json_editor.set_editor(spec)
            self.tag.json_editor.on_editor_change()
            self.tag.current_auto_chart_ind -= 1

    def button_generate_click(self, **event_args):

        chart_params = gen_chart_params()
        c = anvil.confirm(
            chart_params,
            buttons=[("ok", "ok"), ("cancel", "cancel")],
            large=True,
            title="Choose parameters for automatic chart creation",
        )

        if c == "ok" and chart_params.flow_panel_columns.tag.current_cols:

            cols = chart_params.flow_panel_columns.tag.current_cols
            dataset_name = chart_params.drop_down_dataset.selected_value
            survey_row = anvil.get_open_form().tag.row
            chart_schemas = anvil.server.call(
                "data_to_spec", survey_row, cols, dataset_name
            )
            self.build_auto_charts(chart_schemas)

    def build_auto_charts(self, chart_schemas, **event_args):

        if chart_schemas:
            self.tag.auto_charts = chart_schemas
            self.button_right.visible = True
            self.button_left.visible = True
            spec = chart_schemas[0]
            self.tag.json_editor.set_editor(spec)
            self.tag.json_editor.on_editor_change()
            self.tag.current_auto_chart_ind = 0

        else:
            self.button_right.visible = False
            self.button_left.visible = False
            anvil.alert(
                "Please see the docs on automatic chart generation",
                title=(
                    "No charts could be generated given the templates"
                    "and chosen parameters"
                ),
            )

    def button_save_template_click(self, **event_args):

        spec = self.tag.json_editor.get_editor_text_to_json()
        survey_row = anvil.get_open_form().tag.row
        dataset_name = spec["data"]["name"]
        view = self.tag.chart.tag.view
        url = view.toImageURL("png")
        url_media = anvil.URLMedia(url)

        anvil.server.call("spec_to_template", dataset_name, survey_row, spec, url_media)

        msg = (
            "The next time you generate automatic charts, this template will be "
            "considered in the matching process",
        )
        anvil.Notification(
            msg,
            title="This spec has been saved as a template",
        ).show()

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        spec = self.tag.json_editor.get_editor_text_to_json()
        self.tag.chart.call_js("get_vega_png", spec)
