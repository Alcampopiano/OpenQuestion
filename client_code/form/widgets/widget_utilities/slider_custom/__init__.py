from ._anvil_designer import slider_customTemplate


class slider_custom(slider_customTemplate):
    def __init__(self, **properties):
        self._shown = False
        self.init_components(**properties)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.update()

    @property
    def min_val(self):
        return self._min_val

    @min_val.setter
    def min_val(self, value):
        self._min_val = value
        self.update()

    @property
    def max_val(self):
        return self._max_val

    @max_val.setter
    def max_val(self, value):
        self._max_val = value
        self.update()

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value
        self.update()

    #   @property
    #   def level(self):
    #     return self._level

    #   @level.setter
    #   def level(self, value):
    #     self._level = value
    #     self.update()

    def slider_change(self, value, **event_args):
        self._value = int(value)
        self.raise_event("change", level=self.value)

    def update(self):
        if self._shown:
            self.call_js(
                "set_behavior", self.value, self.min_val, self.max_val, self.step
            )

    def form_show(self, **event_args):
        """This method is called when the HTML panel is shown on the screen"""
        self._shown = True
        self.update()
