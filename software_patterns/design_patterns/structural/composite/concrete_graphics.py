from __future__ import annotations

from .graphic_interface import Graphic


class Dot(Graphic):
    """
    The **Leaf** class represents end objects of a composition. A
    **Leaf** object can't have any sub-objects. Usually, it's **Leaf**
    objects that do the actual work, while **Composite** objects only
    delegate to their sub-components.
    """

    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def move(self, x: float, y: float) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(f"Drawing a dot at ({self.x}, {self.y})")


class Circle(Dot):
    """
    All **Component** classes can extend other **Components**.
    """

    radius: float

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y)
        self.radius = radius

    def draw(self) -> None:
        print(f"Drawing a circle at ({self.x}, {self.y}) with radius {self.radius}")


class CompoundGraphic(Graphic):
    """
    The **Composite** class represents complex components that may have
    children. **Composite** objects usually delegate the actual work to their
    children and then "sum up" the result.

    A **Composite** object can add or remove other components (both simple
    and complex) to or from its list of children.
    """

    children: list[Graphic]

    def add(self, child: Graphic) -> None:
        self.children.append(child)

    def remove(self, child: Graphic) -> None:
        self.children.remove(child)

    def move(self, x: float, y: float) -> None:
        for child in self.children:
            child.move(x, y)

    def draw(self) -> None:
        """
        A **Composite** executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and
        summing up their results. Since the **Composite**'s children pass
        these calls to their own children and so forth, the whole object tree
        is traversed as a result.
        """

        for child in self.children:
            child.draw()
            # then update bounding rectangle
        # draw bounding rectangle using bounding coordinates
