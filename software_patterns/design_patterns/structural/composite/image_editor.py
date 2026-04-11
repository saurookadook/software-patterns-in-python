from __future__ import annotations

from typing import TYPE_CHECKING

from .concrete_graphics import CompoundGraphic, Circle, Dot

if TYPE_CHECKING:
    from .graphic_interface import Graphic


class ImageEditor:
    """
    The client code works with all the components via their base interface.
    This way, the client code can support simple **Leaf** components as well
    as complex **Composite** components.
    """

    all: CompoundGraphic

    def load(self) -> None:
        self.all = CompoundGraphic()
        self.all.add(Dot(1, 2))
        self.all.add(Circle(5, 3, 10))
        # ...

    def group_selected(self, components: list[Graphic]) -> None:
        """
        Combine selected components into one complex **Composite** component.
        """
        group = CompoundGraphic()
        for c in components:
            group.add(c)
            self.all.remove(c)
        self.all.add(group)
        self.all.draw()
