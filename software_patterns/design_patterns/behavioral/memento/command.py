from __future__ import annotations

from .editor import Editor
from .snapshot import Snapshot


class Command:
    """A command object can act as a **Caretaker**. In that case, the
    command gets a **Memento** just before it changes the **Originator**'s
    state. When `undo` is requested, it restores the **Originator**'s
    state from a **Memento**.
    """

    def __init__(self, editor: Editor) -> None:
        self._editor = editor
        self._backup: Snapshot | None = None

    def make_backup(self) -> None:
        self._backup = self._editor.create_snapshot()

    def undo(self) -> None:
        if self._backup is not None:
            self._backup.restore()
