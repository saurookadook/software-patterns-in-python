from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .application import Application
    from .editor import Editor


class Command(ABC):
    """
    The base **Command** class defines the common interface for all
    **Concrete Command** classes.
    """

    app: Application
    editor: Editor
    backup: str

    def __init__(self, app: Application, editor: Editor) -> None:
        self.app = app
        self.editor = editor
        self.backup = ""

    def save_backup(self) -> None:
        """Make a backup of the editor's state."""
        self.backup = self.editor.text

    def undo(self) -> None:
        """Restore the editor's state."""
        self.editor.text = self.backup

    @abstractmethod
    def execute(self) -> bool:
        """
        The ``execution`` method is declared abstract to force all
        **Concrete Command** classes to provide their own implementations.
        The method must return ``True`` or ``False`` depending on whether
        the **Command** changes the editor's state.
        """
