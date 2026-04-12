from __future__ import annotations

from abc import ABC, abstractmethod


class EventListener(ABC):
    """
    Here's the **Subscriber** interface. If your programming language
    supports functional types, you can replace the whole **Subscriber**
    hierarchy with a set of functions.
    """

    @abstractmethod
    def update(self, filename: str) -> None: ...
