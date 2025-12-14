from typing import Any

from .concrete_decorators import CompressionDecorator, EncryptionDecorator
from .data_sources import FileDataSource, DataSource
from .salary_data import salary_records


class SalaryManager:
    """Option 2.

    Client code that uses an external data source. `SalaryManager` objects
    neither know nor care about data storage specifics. They work with a
    pre-configured data source received from the app configurator.
    """

    source: DataSource

    def __init__(self, source: DataSource) -> None:
        self.source = source

    def load(self) -> Any:
        return self.source.read_data()

    def save(self, records: Any) -> None:
        self.source.write_data(records)


class ApplicationConfigurator:
    """The app can assemble different stacks of decorators at runtime,
    depending on the configuration or environment.
    """

    compression_enabled: bool = True
    encryption_enabled: bool = True

    def __init__(self, config: dict = dict()) -> None:
        self.compression_enabled = config.get("compression_enabled", True)
        self.encryption_enabled = config.get("encryption_enabled", True)

    def configuration_example(self):
        source = FileDataSource("salary_data.csv")

        if self.compression_enabled:
            source = CompressionDecorator(source)
        if self.encryption_enabled:
            source = EncryptionDecorator(source)

        logger = SalaryManager(source)
        salary = logger.load()
        # ...
