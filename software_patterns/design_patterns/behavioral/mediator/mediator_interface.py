from __future__ import annotations

from abc import ABC, abstractmethod


from .component import Component


class Mediator(ABC):
    """The mediator interface declares a method used by components to notify
    the mediator about various events. The mediator may react to these events
    and pass the execution to other components.
    """

    @abstractmethod
    def notify(self, sender: Component, event: str) -> None:
        pass
