from engines.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_indicator_on):
        self._warning_indicator_on = warning_indicator_on

    def needs_service(self):
        return self._warning_indicator_on
