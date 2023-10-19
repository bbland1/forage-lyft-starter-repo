from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self._engine = engine
        self._battery = battery
        self._tires = tires

    def needs_service(self) -> bool:
        engine_service = self._engine.needs_service()
        battery_service = self._battery.needs_service()
        tires_service = self._tires.needs_service()

        return engine_service or battery_service or tires_service
