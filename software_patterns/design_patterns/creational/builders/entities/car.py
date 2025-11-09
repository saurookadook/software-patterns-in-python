from dataclasses import dataclass

from ..constants import EngineType, SeatsMetadata


@dataclass
class CarConfig:
    engine: EngineType
    install_GPS: bool
    install_trip_computer: bool
    seats: int


class Car:
    """A car can have a GPS, trip computer and some number of \
    seats. Different models of cars (sports car, SUV, \
    cabriolet) might have different features installed or \
    enabled.
    """

    _GPS: bool = False
    _engine: EngineType | None = None
    _seats: int = 0
    _trip_computer: bool = False

    # ---- Getters and Setters ------------------------------------------------
    @property
    def GPS(self):
        return self._GPS

    @GPS.setter
    def GPS(self, value: bool):
        self._GPS = value

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine: EngineType):
        if engine not in EngineType:
            raise ValueError(f"Invalid engine type: '{engine}'")

        self._engine = engine

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, seats: int):
        if seats < SeatsMetadata.MIN_COUNT or seats > SeatsMetadata.MAX_COUNT:
            raise ValueError(
                f"Invalid number of seats: '{seats}'. "
                + f"Must be between {SeatsMetadata.MIN_COUNT} and {SeatsMetadata.MAX_COUNT}."
            )
        self._seats = seats

    @property
    def trip_computer(self):
        return self._trip_computer

    @trip_computer.setter
    def trip_computer(self, value: bool):
        self._trip_computer = value
