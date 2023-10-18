from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    def needs_service(self) -> bool:
        engine_service = self._engine.needs_service()
        battery_service = self._battery.needs_service()

        return engine_service or battery_service
