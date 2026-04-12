from __future__ import annotations

from .command_interface import Command


class CopyCommand(Command):
    """
    The copy command isn't saved to the history since it doesn't
    change the editor's state.
    """

    def execute(self) -> bool:
        self.app.clipboard = self.editor.get_selection()
        return False


class CutCommand(Command):
    """
    The cut command does change the editor's state, therefore it must be
    saved to the history. And it'll be saved as long as the method
    returns ``True``.
    """

    def execute(self) -> bool:
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True


class PasteCommand(Command):
    def execute(self) -> bool:
        self.save_backup()
        self.editor.replace_selection(self.app.clipboard)
        return True


class UndoCommand(Command):
    def execute(self) -> bool:
        self.app.undo()
        return False
