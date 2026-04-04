from __future__ import annotations

from enum import StrEnum

from .concrete_strategies import (
    ConcreteStrategyAdd,
    ConcreteStrategySubtract,
    ConcreteStrategyMultiply,
    ConcreteStrategyDivide,
)
from .context import Context


class Operand(StrEnum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"


class ExampleApplication:
    """The client code picks a ``ConcreteStrategy`` and passes it to the
    ``Context``. The client should be aware of the differences between
    strategies in order to make the right choice.
    """

    @staticmethod
    def main():
        context = Context()

        input_equation = input(
            "Enter a simple equation with two numbers and an operator (e.g., 1 + 2): "
        )
        first_term, operand, second_term = input_equation.split()

        if operand == Operand.ADDITION:
            print(f"Client: Strategy is set to {Operand.ADDITION.name}.")
            context.set_strategy(ConcreteStrategyAdd())
        elif operand == Operand.SUBTRACTION:
            print(f"Client: Strategy is set to {Operand.SUBTRACTION.name}.")
            context.set_strategy(ConcreteStrategySubtract())
        elif operand == Operand.MULTIPLICATION:
            print(f"Client: Strategy is set to {Operand.MULTIPLICATION.name}.")
            context.set_strategy(ConcreteStrategyMultiply())
        elif operand == Operand.DIVISION:
            print(f"Client: Strategy is set to {Operand.DIVISION.name}.")
            context.set_strategy(ConcreteStrategyDivide())

        result = context.execute_strategy(float(first_term), float(second_term))
        print(result)
