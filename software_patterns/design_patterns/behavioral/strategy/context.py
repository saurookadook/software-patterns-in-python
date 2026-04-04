from __future__ import annotations

from .strategy_interface import Strategy


class Context:
    """The ``Context`` defines the interface of interest to clients."""

    strategy: Strategy
    """
    The ``Context`` maintains a reference to one of the ``Strategy`` objects.
    The ``Context`` doesn't know the concrete class of a ``Strategy``.
    It should work with  all ``Strategies`` via the ``Strategy`` interface.
    """

    def set_strategy(self, strategy: Strategy) -> None:
        """Usually, the ``Context`` accepts a strategy through the
        constructor, but also provides a setter so that the ``Strategy``
        can be changed at runtime.
        """
        self.strategy = strategy

    def execute_strategy(self, a: float, b: float) -> float:
        """The ``Context`` delegates some work to the ``Strategy`` object
        instead of implementing multiple versions of the algorithm on its own.
        """
        return self.strategy.execute(a, b)
