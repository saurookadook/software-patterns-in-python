from ..constants import EngineTypes, SeatsMetadata


class Car:
    """A car can have a GPS, trip computer and some number of \
    seats. Different models of cars (sports car, SUV, \
    cabriolet) might have different features installed or \
    enabled.
    """

    _GPS: bool = False
    _engine: EngineTypes | None = None
    _seats: int = 0
    _trip_computer: bool = False

    # ---- Getters and Setters ------------------------------------------------
    @property
    def GPS(self):
        return self._GPS

    @GPS.setter
    def set_GPS(self, value: bool):
        self._GPS = value

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def set_engine(self, engine: EngineTypes):
        if engine not in EngineTypes:
            raise ValueError(f"Invalid engine type: '{engine}'")

        self._engine = engine

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def set_seats(self, seats: SeatsMetadata):
        if seats < SeatsMetadata.MIN_COUNT or seats > SeatsMetadata.MAX_COUNT:
            raise ValueError(
                f"Invalid number of seats: '{seats}'. "
                + f"Must be between {SeatsMetadata.MIN_COUNT} and {SeatsMetadata.MAX_COUNT}."
            )
        self._seats = seats.value

    @property
    def trip_computer(self):
        return self._trip_computer

    @trip_computer.setter
    def set_trip_computer(self, value: bool):
        self._trip_computer = value
