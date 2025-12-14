from typing import Any

from .data_source_decorator import DataSourceDecorator


class ConcreteDecorator(DataSourceDecorator):
    """Concrete decorators must call methods on the wrapped object, but
    may add something of their own to the result. Decorators can execute
    the added behavior either before or after the call to a wrapped object.
    """


class EncryptionDecorator(ConcreteDecorator):
    """Concrete decorator that handles encrypting/decrypting data."""

    def write_data(self, data: Any) -> None:
        """
        1. Encrypt passed data
        2. Pass encrypted data to the wrappee's `write_data` method.
        """
        pass

    def read_data(self) -> Any:
        """
        1. Get data from the wrappee's `read_data` method.
        2. Try to decrypt it if it's encrypted.
        3. Return the result
        """
        pass


class CompressionDecorator(ConcreteDecorator):
    """Concrete decorator that handles compressing/decompressing data."""

    def write_data(self, data: Any) -> None:
        """
        1. Compress passed data.
        2. Pass compressed data to the wrappee's `write_data` method.
        """
        pass

    def read_data(self) -> Any:
        """
        1. Get data from the wrappee's `read_data` method.
        2. Try to decompress it if it's compressed.
        3. Return the result.
        """
        pass
