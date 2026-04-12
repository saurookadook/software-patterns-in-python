from __future__ import annotations


class Editor:
    """
    The editor class has actual text editing operations and plays the role
    of a **Receiver**: all **Commands** end up delegating execution to
    the editor's methods.
    """

    text: str

    def __init__(self) -> None:
        self.text = ""

    def get_selection(self) -> str:
        return self.text

    def delete_selection(self) -> None:
        self.text = ""

    def replace_selection(self, text: str) -> None:
        self.text = text
