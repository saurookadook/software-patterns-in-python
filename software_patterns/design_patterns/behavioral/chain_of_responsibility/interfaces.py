from __future__ import annotations

from abc import ABC, abstractmethod


class ComponentWithContextualHelp(ABC):
    """The **Handler** interface declares a method for executing a request."""

    @abstractmethod
    def showHelp(self) -> None:
        pass
