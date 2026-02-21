from __future__ import annotations

from .editor import Editor


class Snapshot:
    """The **Memento** class stores the past state of the editor."""

    def __init__(
        self,
        editor: Editor,
        text: str,
        curX: int,
        curY: int,
        selection_width: int,
    ) -> None:
        self._editor = editor
        self._text = text
        self._curX = curX
        self._curY = curY
        self._selection_width = selection_width

    def restore(self) -> None:
        """At some point, a previous state of the editor can be restored
        using this **Memento** object.
        """
        self._editor.set_text(self._text)
        self._editor.set_cursor(self._curX, self._curY)
        self._editor.set_selection_width(self._selection_width)
