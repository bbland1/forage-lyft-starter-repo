from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self._current_date = current_date
        self._last_service_date = last_service_date

    def needs_service(self) -> bool:

        years_since_last_service = (self._current_date.year - self._last_service_date.year)

        if self._current_date.month < self._last_service_date.month or (self._current_date.month == self._last_service_date.month and self._current_date.day < self._last_service_date.day):
            years_since_last_service -= 1
            
        return years_since_last_service >= 2