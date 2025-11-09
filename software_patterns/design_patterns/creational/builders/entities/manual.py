from ..constants import EngineType, SeatsMetadata


class Manual:
    """Each car should have a user manual that corresponds to \
    the car's configuration and describes all its features.

    TODO: Could probably move most of this class's implementation to a \
    base class which is extended by both `Car` and `Manual`.
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
    def seats(self, seats: SeatsMetadata):
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
    def trip_computer(self, value: bool):
        self._trip_computer = value
