from __future__ import annotations

from abc import ABC, abstractmethod


class Device(ABC):
    """The 'implementation' interface declares methods common to all
    concrete implementations. It doesn't have to match the abstraction's
    interface. In fact, the two interfaces can be entirely different.
    Typically, the implementation interface provides only primitive
    operations, while the abstraction defines higher-level operations
    based on those primitives.
    """

    _enabled: bool = False
    _volume: int | float = 10
    _channel: int | float = 12.0

    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> int | float:
        pass

    @abstractmethod
    def set_volume(self, percent: int | float) -> None:
        pass

    @abstractmethod
    def get_channel(self) -> int | float:
        pass

    @abstractmethod
    def set_channel(self, channel: int | float) -> None:
        pass


class ConcreteBaseDevice(Device):
    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    def get_volume(self) -> int | float:
        return self._volume

    def set_volume(self, percent: int | float) -> None:
        self._volume = percent

    def get_channel(self) -> int | float:
        return self._channel

    def set_channel(self, channel: int | float) -> None:
        self._channel = channel
