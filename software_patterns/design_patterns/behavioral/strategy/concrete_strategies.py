"""
Concrete strategies implement the algorithm while following the base
``Strategy`` interface. The interface makes them interchangeable in
the ``Context``.
"""

from __future__ import annotations

from .strategy_interface import Strategy


class ConcreteStrategyAdd(Strategy):
    def execute(self, a: float, b: float) -> float:
        return a + b


class ConcreteStrategySubtract(Strategy):
    def execute(self, a: float, b: float) -> float:
        return a - b


class ConcreteStrategyMultiply(Strategy):
    def execute(self, a: float, b: float) -> float:
        return a * b


class ConcreteStrategyDivide(Strategy):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
