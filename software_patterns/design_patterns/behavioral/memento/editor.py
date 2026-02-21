from __future__ import annotations

from .snapshot import Snapshot


class Editor:
    """The **Originator** holds some important data that may change over
    time. It also defines a method for saving its state inside a **Memento**
    and another method for restoring the state from it.
    """

    def __init__(self) -> None:
        self._text = ""
        self._curX = 0
        self._curY = 0
        self._selection_width = 0

    def set_text(self, text: str) -> None:
        self._text = text

    def set_cursor(self, x: int, y: int) -> None:
        self._curX = x
        self._curY = y

    def set_selection_width(self, width: int) -> None:
        self._selection_width = width

    def create_snapshot(self) -> Snapshot:
        """Save current state inside a **Memento**.

        **Memento** is an immutable object; that's why the **Originator**
        passes its state to the **Memento**'s constructor parameters.
        """
        return Snapshot(
            editor=self,
            text=self._text,
            curX=self._curX,
            curY=self._curY,
            selection_width=self._selection_width,
        )
