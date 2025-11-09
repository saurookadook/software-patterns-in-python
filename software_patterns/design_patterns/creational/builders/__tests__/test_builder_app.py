import pytest

from software_patterns.design_patterns.creational.builders.constants import EngineType
from software_patterns.design_patterns.creational.builders.entities import (
    Car,
    CarConfig,
    Manual,
)
from software_patterns.design_patterns.creational.builders import BuilderApp

test_cases = [
    dict(
        test_name="handles car configs for diesel cars",
        car_configs=[
            CarConfig(
                engine=EngineType.DIESEL,
                install_GPS=False,
                install_trip_computer=True,
                seats=5,
            ),
            CarConfig(
                engine=EngineType.DIESEL,
                install_GPS=True,
                install_trip_computer=True,
                seats=8,
            ),
            CarConfig(
                engine=EngineType.DIESEL,
                install_GPS=False,
                install_trip_computer=False,
                seats=2,
            ),
            CarConfig(
                engine=EngineType.DIESEL,
                install_GPS=True,
                install_trip_computer=False,
                seats=5,
            ),
            CarConfig(
                engine=EngineType.DIESEL,
                install_GPS=True,
                install_trip_computer=False,
                seats=7,
            ),
        ],
    ),
    dict(
        test_name="handles car configs for electric cars",
        car_configs=[
            CarConfig(
                engine=EngineType.ELECTRIC,
                install_GPS=False,
                install_trip_computer=True,
                seats=5,
            ),
            CarConfig(
                engine=EngineType.ELECTRIC,
                install_GPS=True,
                install_trip_computer=True,
                seats=8,
            ),
            CarConfig(
                engine=EngineType.ELECTRIC,
                install_GPS=False,
                install_trip_computer=True,
                seats=2,
            ),
            CarConfig(
                engine=EngineType.ELECTRIC,
                install_GPS=True,
                install_trip_computer=True,
                seats=4,
            ),
        ],
    ),
    dict(
        test_name="handles car configs for gasoline cars",
        car_configs=[
            CarConfig(
                engine=EngineType.GASOLINE,
                install_GPS=False,
                install_trip_computer=False,
                seats=2,
            ),
            CarConfig(
                engine=EngineType.GASOLINE,
                install_GPS=True,
                install_trip_computer=False,
                seats=7,
            ),
            CarConfig(
                engine=EngineType.GASOLINE,
                install_GPS=True,
                install_trip_computer=True,
                seats=5,
            ),
            CarConfig(
                engine=EngineType.GASOLINE,
                install_GPS=False,
                install_trip_computer=True,
                seats=4,
            ),
        ],
    ),
    dict(
        test_name="handles car configs with mix of valid settings",
        car_configs=[
            CarConfig(
                engine=EngineType.ELECTRIC,
                install_GPS=False,
                install_trip_computer=True,
                seats=5,
            ),
            CarConfig(
                engine=EngineType.ELECTRIC,
                install_GPS=True,
                install_trip_computer=True,
                seats=8,
            ),
            CarConfig(
                engine=EngineType.GASOLINE,
                install_GPS=False,
                install_trip_computer=False,
                seats=2,
            ),
            CarConfig(
                engine=EngineType.DIESEL,
                install_GPS=True,
                install_trip_computer=False,
                seats=5,
            ),
            CarConfig(
                engine=EngineType.GASOLINE,
                install_GPS=True,
                install_trip_computer=False,
                seats=7,
            ),
        ],
    ),
]


@pytest.fixture
def builder_app():
    return BuilderApp()


@pytest.mark.parametrize(
    "test_case",
    [tuple(v for v in tc.values()) for tc in test_cases],
)
def test_builder_app(builder_app, test_case):
    _, configs = test_case
    builder_app.make_cars(configs)

    result_products = builder_app.get_result_products()

    assert len(result_products) == len(configs)

    for i, product in enumerate(result_products):
        config = configs[i]
        car, manual = product
        print(f"    {i=}    ".center(120, "="))
        print(f"all configs: {configs=}")
        print(f"{config=} || {car=} || {manual=}")

        assert isinstance(car, Car)
        assert isinstance(manual, Manual)

        for prod in (car, manual):
            assert prod.engine == config.engine
            assert prod.GPS == config.install_GPS
            assert prod.trip_computer == config.install_trip_computer
            assert prod.seats == config.seats
