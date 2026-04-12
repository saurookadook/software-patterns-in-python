from __future__ import annotations

from uuid import UUID

from .concrete_iterator import FacebookIterator
from .interfaces import ProfileIterator, SocialNetwork


class Facebook(SocialNetwork):
    """
    Each **Concrete Collection** is coupled to a set of **Concrete Iterator**
    classes it returns. But the **Client** isn't since the signature of
    these methods returns **Iterator** interfaces.
    """

    # ... bulk of collection's code should go here ...

    def create_friends_iterator(self, profile_id: UUID) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id: UUID) -> ProfileIterator:
        return FacebookIterator(self, profile_id, "coworkers")
