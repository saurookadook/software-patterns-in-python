from __future__ import annotations

from abc import ABC, abstractmethod


class Strategy(ABC):
    """The ``Strategy`` interface declares operations common to all
    supported versions of some algorithm. The context uses this interface
    to call the algorithm defined by the concrete strategies.
    """

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass
