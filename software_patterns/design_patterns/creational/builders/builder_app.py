from typing import List, Tuple

from .car_builder import CarBuilder
from .car_manual_builder import CarManualBuilder
from .entities import Builder, Car, CarConfig, Director, Manual


class BuilderApp:
    """The client code creates a builder object, passes it to the \
    director and then initiates the construction process. The end result is \
    retrieved from the builder object.
    """

    builder: Builder | None
    director: Director
    result_products: List[Tuple[Car, Manual]]

    def __init__(self):
        self.builder = None
        self.director = Director()
        self.result_products = []

    def make_cars(self, car_configs: List[CarConfig]) -> None:
        # TODO: better validation here?
        if car_configs is None or len(car_configs) <= 0:
            raise ValueError("Argument 'car_configs' must be a non-empty list!")

        for config in car_configs:
            self.builder = CarBuilder()
            self.director.construct_car_from_config(self.builder, config)
            car = self.builder.get_product()

            self.builder = CarManualBuilder()
            self.director.construct_car_from_config(self.builder, config)
            manual = self.builder.get_product()

            self.result_products.append((car, manual))

    def get_result_products(self) -> List[Tuple[Car, Manual]]:
        return self.result_products
