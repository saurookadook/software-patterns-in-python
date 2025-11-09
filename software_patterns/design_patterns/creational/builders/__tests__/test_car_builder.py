import pytest

from software_patterns.design_patterns.creational.builders import CarBuilder
from software_patterns.design_patterns.creational.builders.constants import EngineType


@pytest.fixture
def car_builder():
    return CarBuilder()


def test_car_builder_get_and_set_engine(car_builder):
    builder_car = car_builder._car

    assert builder_car.engine == None
    assert car_builder.get_engine() == None

    car_builder.set_engine(EngineType.ELECTRIC)

    assert builder_car.engine == EngineType.ELECTRIC
    assert car_builder.get_engine() == EngineType.ELECTRIC


def test_car_builder_get_and_set_GPS(car_builder):
    builder_car = car_builder._car

    assert builder_car.GPS == False
    assert car_builder.get_GPS() == False

    car_builder.set_GPS(True)

    assert builder_car.GPS == True
    assert car_builder.get_GPS() == True


def test_car_builder_get_and_set_seats(car_builder):
    builder_car = car_builder._car

    assert builder_car.seats == 0
    assert car_builder.get_seats() == 0

    car_builder.set_seats(7)

    assert builder_car.seats == 7
    assert car_builder.get_seats() == 7


def test_car_builder_get_and_set_trip_computer(car_builder):
    builder_car = car_builder._car

    assert builder_car.trip_computer == False
    assert car_builder.get_trip_computer() == False

    car_builder.set_trip_computer(True)

    assert builder_car.trip_computer == True
    assert car_builder.get_trip_computer() == True
