from software_patterns.design_patterns.creational.builders.constants import (
    EngineType,
    SeatsMetadata,
)
from software_patterns.design_patterns.creational.builders.entities.car import CarConfig


class Director:
    """The director is only responsible for executing the building \
    steps in a particular sequence. It's helpful when producing products \
    according to a specific order or configuration. Strictly speaking, the \
    director class is optional, since the client can control builders directly.

    The director works with any builder instance that the client code passes \
    to it. This way, the client code may alter the final type of the newly \
    assembled product. The director can construct several product variations \
    using the same building steps.
    """

    def construct_car_from_config(self, builder, config):
        builder.reset()
        builder.set_engine(config.engine)
        builder.set_GPS(config.install_GPS)
        builder.set_seats(config.seats)
        builder.set_trip_computer(config.install_trip_computer)

    def construct_basic_diesel_car(self, builder):
        self.construct_car_from_config(
            builder,
            CarConfig(
                engine=EngineType.DIESEL,
                install_GPS=False,
                install_trip_computer=False,
                seats=SeatsMetadata.MIN_COUNT,
            ),
        )

    def construct_basic_electric_car(self, builder):
        self.construct_car_from_config(
            builder,
            CarConfig(
                engine=EngineType.ELECTRIC,
                install_GPS=True,
                install_trip_computer=True,
                seats=SeatsMetadata.STANDARD_COUNT,
            ),
        )

    def construct_basic_gasoline_car(self, builder):
        self.construct_car_from_config(
            builder,
            CarConfig(
                engine=EngineType.GASOLINE,
                install_GPS=True,
                install_trip_computer=False,
                seats=SeatsMetadata.MAX_COUNT,
            ),
        )
