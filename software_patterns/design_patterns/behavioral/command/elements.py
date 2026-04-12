from __future__ import annotations

from typing import Callable

CallbackFn = Callable[[], None]


class Button:
    command: CallbackFn

    def set_command(self, command: CallbackFn) -> None:
        self.command = command


class ShortcutsRegistry:
    callbacks_map: dict[str, list[CallbackFn]]

    def on_key_press(self, event_type: str, command: CallbackFn) -> None:
        if event_type not in self.callbacks_map:
            self.callbacks_map[event_type] = []
        self.callbacks_map[event_type].append(command)
