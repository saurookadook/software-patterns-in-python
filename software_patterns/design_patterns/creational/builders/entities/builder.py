from typing import Any

from software_patterns.design_patterns.creational.builders.constants import EngineType


class Builder:

    class MethodNotImplemented(NotImplementedError):
        pass

    def reset(self) -> None:
        raise Builder.MethodNotImplemented()

    def set_seats(self, seats: int) -> None:
        raise Builder.MethodNotImplemented()

    def set_engine(self, engine_type: EngineType) -> None:
        raise Builder.MethodNotImplemented()

    def set_GPS(self, should_have_GPS: bool) -> None:
        raise Builder.MethodNotImplemented()

    def get_product(self) -> Any:
        raise Builder.MethodNotImplemented()
