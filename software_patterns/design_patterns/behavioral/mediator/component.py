from __future__ import annotations

from .mediator_interface import Mediator


class Component:
    """Components communicate with a mediator using the mediator interface.
    Thanks to that, you can use the same comopnents in other contexts by
    linking them with different mediator objects.
    """

    def __init__(self, dialog: Mediator) -> None:
        self.dialog = dialog

    def click(self) -> None:
        self.dialog.notify(self, "click")

    def keypress(self) -> None:
        self.dialog.notify(self, "keypress")
