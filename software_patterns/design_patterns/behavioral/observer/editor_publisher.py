from __future__ import annotations

from pathlib import Path

from .event_manager_publisher import EventManager


class Editor:
    """
    The **Concrete Publisher** contains real business logic that's
    interesting for some **Subscribers**. We could derive this class from
    the base **Publisher**, but that isn't always possible in real life
    because the **Concrete Publisher** might already be a subclass. In this
    case, you can patch the subscription logic in with composition, as we
    did here.
    """

    events: EventManager
    file: Path

    def __init__(self) -> None:
        self.events = EventManager()

    def open_file(self, file_path: str) -> None:
        """
        Methods of business logic can notify subscribers about changes.
        """
        self.file = Path(file_path)
        self.events.notify("open", self.file.name)

    def save_file(self) -> None:
        with open(self.file, "w") as file:
            file.write("whatever stuff we haven't saved yet")
            self.events.notify("save", self.file.name)
