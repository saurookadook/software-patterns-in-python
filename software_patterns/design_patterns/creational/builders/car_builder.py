from software_patterns.design_patterns.creational.builders.constants import EngineType
from software_patterns.design_patterns.creational.builders.entities import Builder, Car


class CarBuilder(Builder):
    """The concrete builder classes follow the builder interface \
    and provide specific implementations of the building steps. Your \
    program may have program may have several variations of builders, each \
    implemented differently.
    """

    _car: Car

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    def get_seats(self) -> int:
        return self._car.seats

    def set_seats(self, seats: int) -> None:
        self._car.seats = seats

    def get_engine(self) -> EngineType | None:
        return self._car.engine

    def set_engine(self, engine_type: EngineType) -> None:
        self._car.engine = engine_type

    def get_trip_computer(self) -> bool:
        return self._car.trip_computer

    def set_trip_computer(self, should_have_trip_computer: bool) -> None:
        self._car.trip_computer = should_have_trip_computer

    def get_GPS(self) -> bool:
        return self._car.GPS

    def set_GPS(self, should_have_GPS: bool) -> None:
        self._car.GPS = should_have_GPS

    def get_product(self) -> Car:
        """Concrete builders are supposed to provide their own \
        methods for retrieving results. That's because various \
        types of builders may create entirely different products \
        that don't all follow the same interface. Therefore such \
        methods can't be declared in the builder interface (at \
        least not in a statically-typed programming language). \

        Usually, after returning the end result to the client, a \
        builder instance is expected to be ready to start \
        producing another product. That's why it's a usual \
        practice to call the reset method at the end of the \
        `getProduct` method body. However, this behavior isn't \
        mandatory, and you can make your builder wait for an \
        explicit reset call from the client code before disposing \
        of the previous result.
        """

        product = self._car
        self.reset()
        return product
