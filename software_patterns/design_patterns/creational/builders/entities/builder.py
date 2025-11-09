from typing import Any

from software_patterns.design_patterns.creational.builders.constants import EngineType


class Builder:

    class NotImplementedError(Exception):
        pass

    def reset(self) -> None:
        raise Builder.NotImplementedError()

    def set_seats(self, seats: int) -> None:
        raise Builder.NotImplementedError()

    def set_engine(self, engine_type: EngineType) -> None:
        raise Builder.NotImplementedError()

    def set_GPS(self, should_have_GPS: bool) -> None:
        raise Builder.NotImplementedError()

    def get_product(self) -> Any:
        raise Builder.NotImplementedError()
