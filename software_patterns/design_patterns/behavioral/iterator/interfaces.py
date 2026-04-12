from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any
from uuid import UUID

if TYPE_CHECKING:
    from .concrete_iterator import Profile


class ProfileIterator(ABC):
    """
    The common interface for all **Concrete Iterators**.
    """

    @abstractmethod
    def get_next(self) -> Profile | None: ...

    @abstractmethod
    def has_more(self) -> bool: ...


class SocialNetwork(ABC):
    """
    The **Collection** interface must declare a factory method for
    producing **Iterator** objects. You can declare several methods if there
    are different kinds of iteration available in your program.
    """

    @abstractmethod
    def create_friends_iterator(self, profile_id: UUID) -> ProfileIterator: ...

    @abstractmethod
    def create_coworkers_iterator(self, profile_id: UUID) -> ProfileIterator: ...
