from typing import Any

from .data_sources import DataSource


class DataSourceDecorator(DataSource):
    """The base decorator class follows the same interface as the other
    components. The primary purpose of this class is to define the wrapping
    interface for all concrete decorators. The default implementation of the
    wrapping code might include a field for storing a wrapped component and
    the means to initialize it.
    """

    _wrappee: DataSource

    def __init__(self, source: DataSource) -> None:
        self._wrappee = source

    def write_data(self, data: Any) -> None:
        """The base decorator simply delegates all work to the wrapped
        component. Extra behaviors can be added in concrete decorators.
        """

        self._wrappee.write_data(data)

    def read_data(self) -> Any:
        """Concrete decorators may call the parent implementation of
        the operation instead of calling the wrapped object directly.
        This approach simplifies extension of decorator classes.
        """

        return self._wrappee.read_data()
