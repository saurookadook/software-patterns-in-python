from __future__ import annotations

from pathlib import Path

from .event_listener_interface import EventListener


class LoggingListener(EventListener):
    """
    **Concrete Subscribers** react to updates issued by the
    **Publisher** to which they are attached.
    """

    log: Path
    message: str

    def __init__(self, log_filename: str, message: str) -> None:
        self.log = Path(log_filename)
        self.log.touch(exist_ok=True)
        self.message = message

    def update(self, filename: str) -> None:
        with open(self.log, "a") as log_file:
            log_file.write(f"Someone has changed the file: {filename}\n")


class EmailAlertsListener(EventListener):
    """
    **Concrete Subscribers** react to updates issued by the
    **Publisher** to which they are attached.
    """

    email: str
    message: str

    def __init__(self, email: str, message: str) -> None:
        self.email = email
        self.message = message

    def update(self, filename: str) -> None:
        system.email(self.email, filename, self.message)  # type: ignore
