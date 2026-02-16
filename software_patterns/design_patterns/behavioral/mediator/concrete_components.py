"""Concrete components don't talk to each other. They have only one
communication channel, which is sending notifications to the mediator.
"""

from __future__ import annotations

from .component import Component


class Button(Component):
    pass


class Textbox(Component):
    pass


class Checkbox(Component):
    def check(self) -> None:
        self.dialog.notify(self, "check")
