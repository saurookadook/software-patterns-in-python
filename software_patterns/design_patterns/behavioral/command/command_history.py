from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .command_interface import Command


class CommandHistory:
    """
    The global **Command History** is just a stack.
    """

    history: list[Command]

    def __init__(self) -> None:
        self.history = []

    def push(self, c: Command) -> None:
        self.history.append(c)

    def pop(self) -> Command:
        return self.history.pop()
