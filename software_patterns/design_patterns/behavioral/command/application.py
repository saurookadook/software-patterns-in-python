from __future__ import annotations

from typing import TYPE_CHECKING

from .command_history import CommandHistory
from .concrete_commands import CopyCommand, CutCommand, PasteCommand, UndoCommand
from .editor import Editor
from .elements import Button, ShortcutsRegistry

if TYPE_CHECKING:
    from .command_interface import Command


class Application:
    """
    The application class sets up object relations and plays the role
    of a **Sender**: when something neeeds to be done, it creates a
    **Command** object and executes it.
    """

    clipboard: str
    active_editor: Editor
    editors: list[Editor]
    history: CommandHistory
    copy_button: Button
    cut_button: Button
    paste_button: Button
    undo_button: Button
    shortcuts: ShortcutsRegistry

    def __init__(self) -> None:
        self.clipboard = ""
        self.active_editor = Editor()
        self.editors = [self.active_editor]
        self.history = CommandHistory()
        self.copy_button = Button()
        self.cut_button = Button()
        self.paste_button = Button()
        self.undo_button = Button()
        self.shortcuts = ShortcutsRegistry()

    def create_ui(self) -> None:
        """
        The code which assigns commands to UI objects may look like this.
        """
        copy_fn = lambda: self.execute_command(CopyCommand(self, self.active_editor))
        self.copy_button.set_command(copy_fn)
        self.shortcuts.on_key_press("Ctrl+C", copy_fn)

        cut_fn = lambda: self.execute_command(CutCommand(self, self.active_editor))
        self.cut_button.set_command(cut_fn)
        self.shortcuts.on_key_press("Ctrl+X", cut_fn)

        paste_fn = lambda: self.execute_command(PasteCommand(self, self.active_editor))
        self.paste_button.set_command(paste_fn)
        self.shortcuts.on_key_press("Ctrl+V", paste_fn)

        undo_fn = lambda: self.execute_command(UndoCommand(self, self.active_editor))
        self.undo_button.set_command(undo_fn)
        self.shortcuts.on_key_press("Ctrl+Z", undo_fn)

    def execute_command(self, command: Command) -> None:
        """
        Execute a **Command** and check whether it has to be added to
        the hsitory.
        """
        if command.execute():
            self.history.push(command)

    def undo(self) -> None:
        """
        Take the most recent **Command** from the history and run its
        ``undo`` method. Note that we don't know the class of that
        **Command**. But we don't have to, since **Command** knows how
        to undo its own action.
        """
        command = self.history.pop()
        if command is not None:
            command.undo()
