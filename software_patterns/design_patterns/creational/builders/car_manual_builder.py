from .constants import EngineType
from .entities import Builder, Manual


class CarManualBuilder(Builder):
    _manual: Manual

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._manual = Manual()

    def get_seats(self) -> int:
        return self._manual.seats

    def set_seats(self, seats: int) -> None:
        self._manual.seats = seats

    def get_engine(self) -> EngineType | None:
        return self._manual.engine

    def set_engine(self, engine_type: EngineType) -> None:
        self._manual.engine = engine_type

    def get_trip_computer(self) -> bool:
        return self._manual.trip_computer

    def set_trip_computer(self, should_have_trip_computer: bool) -> None:
        self._manual.trip_computer = should_have_trip_computer

    def get_GPS(self) -> bool:
        return self._manual.GPS

    def set_GPS(self, should_have_GPS: bool) -> None:
        self._manual.GPS = should_have_GPS

    def get_product(self) -> Manual:
        product = self._manual
        self.reset()
        return product
