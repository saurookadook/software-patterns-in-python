from __future__ import annotations

from abc import ABC, abstractmethod

Position = tuple[float, float]


class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.center: Position = (self.width / 2, self.height / 2)


class Structure:
    def collect(self) -> None:
        print("Collecting resources...")


class Unit:
    def __init__(self, position: Position = (0, 0)) -> None:
        self.position = position


class GameAI(ABC):
    """
    The ``AbstractClass`` defines a **template method** that contains a skeleton
    of some algorithm composed of calls, usually to abstract operations.
    Concrete subclasses implement these operations, but leave the
    **template method** itself intact.
    """

    def __init__(self, game_map: Map) -> None:
        self.game_map = game_map
        self.built_structures: list[Structure] = []
        self.resources: list[int] = []
        self.scouts: list[Unit] = []
        self.warriors: list[Unit] = []

    def take_turn(self) -> None:
        """The **template method** defines the skeleton of an algorithm."""
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()

    # Some of the steps may be implemented in the base class.
    def collect_resources(self) -> None:
        for structure in self.built_structures:
            structure.collect()

    # And some of them may be defined as abstract.
    @abstractmethod
    def build_structures(self) -> None: ...
    @abstractmethod
    def build_units(self) -> None: ...

    def attack(self) -> None:
        """A class can have several **template methods**."""
        enemy = self.closest_enemy()
        if enemy is None:
            self.send_scouts(self.game_map.center)
        else:
            self.send_warriors(enemy.position)

    @abstractmethod
    def send_scouts(self, position: Position) -> None: ...
    @abstractmethod
    def send_warriors(self, position: Position) -> None: ...

    def closest_enemy(self) -> Unit | None:
        print("Finding closest enemy...")


class OrcsAI(GameAI):
    """``ConcreteClasses`` have to implement all abstract operations of the
    base class but they must not override the **template method** itself.
    """

    def build_structures(self) -> None:
        if len(self.resources) > 25:
            print("Build farms, then barracks, then stronghold.")

    def build_units(self) -> None:
        if len(self.resources) > 50:
            if len(self.scouts) <= 0:
                print("Build peon, add it to scouts group.")
            else:
                print("Build grunt, add it to warriors group.")

    def send_scouts(self, position: Position) -> None:
        if len(self.scouts) > 0:
            print(f"Sending scouts to {position}.")

    def send_warriors(self, position: Position) -> None:
        if len(self.warriors) > 0:
            print(f"Sending warriors to {position}.")


class MonstersAI(GameAI):
    """Subclasses can also override some operations with a default implementation."""

    def collect_structures(self) -> None:
        print("Monsters don't collect structures.")

    def build_structures(self) -> None:
        print("Monsters don't build structures.")

    def build_units(self) -> None:
        print("Monsters don't build units.")
