from __future__ import annotations

from typing import Optional

from .interfaces import ComponentWithContextualHelp


class Component(ComponentWithContextualHelp):
    """The base class for simple components.

    The component's ``container`` acts as the next link in the
    chain of **Handlers**.
    """

    container: Optional[Container]
    height: Optional[int]
    tooltipText: Optional[str]
    width: Optional[int]
    x: Optional[int]
    y: Optional[int]

    def __init__(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        tooltipText: Optional[str] = None,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tooltipText = tooltipText

    def showHelp(self) -> None:
        """The component shows a tooltip if there's help text assigned to it.
        Otherwise, it forwards the call to the container, if it exists.
        """

        if self.tooltipText is not None:
            print(f"Tooltip: {self.tooltipText}")
        elif isinstance(self.container, Container):
            self.container.showHelp()


class Container(Component):
    """Containers can contain both simple components and other containers
    as children. The chain relationships are established here. The class
    inherits ``showHelp`` behavior from its parent.
    """

    children: list[Component]

    def __init__(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        tooltipText: Optional[str] = None,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
            tooltipText=tooltipText,
        )
        self.children = []

    def add(self, child: Component) -> None:
        self.children.append(child)
        child.container = self


class Button(Component):
    """Primitive components may be fine with default help implementation..."""


class Panel(Container):
    """But complex components may override the default implementation.
    If the help text can't be provided in a new way, the component can
    always call the base implementation (see ``Component`` class).
    """

    modalHelpText: Optional[str]

    def showHelp(self) -> None:
        if self.modalHelpText is not None:
            print(f"Modal help: {self.modalHelpText}")
        else:
            super().showHelp()


class Dialog(Container):
    """Same behavior as ``Panel``, but with a wiki page URL."""

    wikiPageURL: Optional[str]

    def showHelp(self) -> None:
        if self.wikiPageURL is not None:
            print(f"Wiki page: {self.wikiPageURL}")
        else:
            super().showHelp()
