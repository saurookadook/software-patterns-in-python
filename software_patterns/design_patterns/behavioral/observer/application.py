from __future__ import annotations

from .concrete_listeners import EmailAlertsListener, LoggingListener
from .editor_publisher import Editor


class Application:
    """
    An application can configure **Publishers** and **Subscribers** at runtime.
    """

    editor: Editor

    def config(self) -> None:
        self.editor = Editor()

        logger = LoggingListener(
            "/path/to/log.txt",
            "Someone has opened the file: %s",
        )
        self.editor.events.subscribe("open", logger)

        email_alerts = EmailAlertsListener(
            "admin@example.com",
            "Someone has changed the file: %s",
        )
        self.editor.events.subscribe("save", email_alerts)
