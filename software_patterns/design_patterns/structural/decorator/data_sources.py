from typing import Any


class DataSource:
    """The component interface defines operations that can be
    altered by decorators.
    """

    class MethodNotImplemented(NotImplementedError):
        pass

    def write_data(self, data: Any) -> None:
        raise DataSource.MethodNotImplemented()

    def read_data(self) -> Any:
        raise DataSource.MethodNotImplemented()


class FileDataSource(DataSource):
    """Concrete components provide default implementations for the
    operations. There might be several variations of those classes
    in a program.
    """

    def __init__(self, filename: str) -> None:
        self._filename = filename

    def write_data(self, data: Any) -> None:
        pass

    def read_data(self) -> Any:
        pass
