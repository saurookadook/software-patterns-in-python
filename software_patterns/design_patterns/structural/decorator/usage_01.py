from .concrete_decorators import CompressionDecorator, EncryptionDecorator
from .data_sources import FileDataSource
from .salary_data import salary_records


class Application:
    """Option 1.

    A simple example of a decorator assembly.
    """

    def simplistic_usage_example(self):
        source = FileDataSource("some_file.csv")
        source.write_data(salary_records)
        # Target file has been written with plain data.

        source = CompressionDecorator(source)
        source.write_data(salary_records)
        # Target file has been written with compressed data.

        source = EncryptionDecorator(source)
        # The source variable now contains this:
        # Encryption > Compression > FileDataSource
        source.write_data(salary_records)
        # File has been written with compressed and encrypted data.
