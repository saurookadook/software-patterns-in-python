from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, overload

if TYPE_CHECKING:
    from .audio_player import AudioPlayer


class State(ABC):
    """
    The base ``State`` class declares methods that all ``ConcreteStates``
    should implement and also provides a backreference to the ``Context``
    object associated with the ``State``. ``States`` can use the
    backreference to transition the ``Context`` to another ``State``.
    """

    player: AudioPlayer

    def __init__(self, player: AudioPlayer) -> None:
        """
        ``Context`` passes itself to the ``State`` concstructor. This may
        help a ``State`` fetch some useful ``Context`` data if it's needed.
        """

        self.player = player

    @abstractmethod
    def click_lock(self) -> None: ...

    @abstractmethod
    def click_play(self) -> None: ...

    @abstractmethod
    def click_next(self) -> None: ...

    # @overload
    # @abstractmethod
    # def click_next(self) -> None: ...
    # @overload
    # @abstractmethod
    # def click_next(self, event: Any) -> None: ...

    @abstractmethod
    def click_previous(self) -> None: ...

    # @overload
    # @abstractmethod
    # def click_previous(self) -> None: ...
    # @overload
    # @abstractmethod
    # def click_previous(self, event: Any) -> None: ...
