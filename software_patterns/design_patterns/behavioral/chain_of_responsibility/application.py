from __future__ import annotations

from typing import Optional

from .components import Button, Dialog, Panel


class Application:
    """Client code.

    Every application configures the chain differently.
    """

    cancel_button: Optional[Button]
    dialog: Optional[Dialog]
    ok_button: Optional[Button]
    panel: Optional[Panel]

    def __init__(
        self,
        dialog: Optional[Dialog] = None,
        panel: Optional[Panel] = None,
        ok_button: Optional[Button] = None,
        cancel_button: Optional[Button] = None,
    ) -> None:
        self.dialog = dialog
        self.panel = panel
        self.ok_button = ok_button
        self.cancel_button = cancel_button

    def createUI(self) -> None:
        self.dialog = Dialog(tooltipText="Budget Reports")
        self.dialog.wikiPageURL = "https://www.example.com/wiki/budget-reports"
        self.panel = Panel(0, 0, 400, 800)
        self.panel.modalHelpText = "This panel does some stuff with budget reporsts."
        self.ok_button = Button(250, 760, 50, 20, "OK")
        self.ok_button.tooltipText = "This is a button that confirms something."
        self.cancel_button = Button(320, 760, 50, 20, "Cancel")
        self.cancel_button.tooltipText = "This is a button that cancels something."
        # ...
        self.panel.add(self.ok_button)
        self.panel.add(self.cancel_button)
        self.dialog.add(self.panel)

    def onF1KeyPress(self) -> None:
        """Imagine what happens here."""

        self.component = self.get_component_at_mouse_coords()  # type: ignore
        self.component.showHelp()
