import anvil.http
import anvil.server
import anvil

from ... import reports
from .. import widgets
from ...utilities import augment
from ..widgets.widget_utilities.data_info_view import data_info_view
import anvil.http
from ._anvil_designer import mainTemplate


class main(mainTemplate):
    def __init__(self, row, **properties):

        self.init_components(**properties)

        file_loader = anvil.FileLoader(multiple=True, file_types=".csv")
        file_loader.set_event_handler("change", self.file_loader_change)
        augment.add_event(file_loader, "click")
        self.tag.file_loader = file_loader

        self.tag.row = row
        vl_schema = anvil.http.request(
            "https://vega.github.io/schema/vega-lite/v4.json", json=True
        )

        vl_schema["definitions"]["HexColor"]["format"] = "uri"
        self.tag.vl_schema = vl_schema

        save_button = anvil.Button(text="save", role="primary-color")
        save_button.set_event_handler("click", self.save_click)
        self.add_component(save_button)

    def save_click(self, **event_args):
        schema, chart_dict = reports.build_schema(self.column_panel)
        datasets = self.tag.data_dicts

        row = anvil.server.call(
            "save_report", self.tag.row, schema, chart_dict, datasets
        )

        self.tag.row = row

    def form_show(self, **event_args):

        row = self.tag.row
        if not row["reports"]:

            # first time in report module
            self.tag.form_dict = {}
            self.tag.data_dicts = anvil.server.call(
                "return_datasets", [row["submissions"]]
            )
            self.tag.num_widgets = 0
            self.link_datasets.text = str(len(self.tag.data_dicts))
            self.section_widget_click()
            self.save_click()

        else:

            # subsequesnt time visiting the report module
            self.tag.data_dicts = row["reports"]["datasets"]

            # update datasets to current state of core data
            current_core_data = anvil.server.call(
                "return_datasets", [row["submissions"]]
            )
            self.tag.data_dicts.update(
                {"records.csv": current_core_data["records.csv"]}
            )
            self.link_datasets.text = str(len(self.tag.data_dicts))
            self.tag.num_widgets = row["reports"]["schema"]["num_widgets"]
            self.text_box_title.text = row["reports"]["title"]
            reports.build_report(
                row["reports"]["schema"], row["reports"]["charts"], self.column_panel
            )

            last_section = self.column_panel.get_components()[-1]
            last_section.section_select()

    def markdown_widget_click(self, **event_args):
        """This method is called when the link is clicked"""
        comp = widgets.markdown(section=self.tag.active_section)
        self.tag.active_section.column_panel.add_component(comp)
        comp.label_id.text = self.tag.num_widgets
        self.tag.num_widgets += 1
        self.tag.form_dict[comp.label_id.text] = comp

    def section_widget_click(self, **event_args):
        section = widgets.section()
        self.column_panel.add_component(section)
        section.label_id.text = self.tag.num_widgets
        self.tag.num_widgets += 1
        self.tag.form_dict[section.label_id.text] = section

    def chart_widget_click(self, **event_args):

        if self.tag.data_dicts:
            comp = widgets.chart(section=self.tag.active_section)
            self.tag.active_section.column_panel.add_component(comp)
            comp.label_id.text = self.tag.num_widgets
            self.tag.num_widgets += 1
            self.tag.form_dict[comp.label_id.text] = comp

        else:
            self.link_datasets_click()

    def file_loader_change(self, files, **event_args):

        if files:
            datasets = [self.tag.row["submissions"]] + files
            data_dicts = anvil.server.call("return_datasets", datasets)
            self.tag.data_dicts = data_dicts

        self.link_datasets.text = str(len(self.tag.data_dicts))

    def link_datasets_click(self, **event_args):
        self.tag.file_loader.trigger("click")

    def link_download_click(self, **event_args):

        m = anvil.server.call("make_html_report", self.tag.row)
        anvil.download(m)

    def link_home_click(self, **event_args):
        anvil.open_form("landing.select_action_survey")

    def link_info_click(self, **event_args):
        """This method is called when the link is clicked"""
        data_dicts = self.tag.data_dicts
        anvil.alert(data_info_view(data_dicts), large=True, buttons=[("ok", "ok")])

    def link_templates_click(self, **event_args):
        anvil.open_form("reports.edit_templates", survey_row=self.tag.row)
