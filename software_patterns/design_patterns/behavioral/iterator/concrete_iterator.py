from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from .interfaces import ProfileIterator

if TYPE_CHECKING:
    from .concrete_collection import Facebook


class Profile:
    profile_id: UUID
    email: str


class FacebookIterator(ProfileIterator):
    """
    The **Concrete Iterator** class.
    """

    facebook: Facebook
    """
    The **Iterator** needs a reference to the **Collection** that it traverses.
    """

    profile_id: UUID
    iter_type: str

    current_position: int
    """
    An **Iterator** object traverses the **Collection** independently from
    other **Iterators**. Therefore, it has to store the iteration state.
    """

    cache: list[Profile]

    def __init__(self, facebook: Facebook, profile_id: UUID, iter_type: str) -> None:
        self.facebook = facebook
        self.profile_id = profile_id
        self.iter_type = iter_type

    def lazy_init(self) -> None:
        if not self.cache:
            self.cache = self.facebook.social_graph_request(  # type: ignore
                self.profile_id, self.iter_type
            )

    def get_next(self) -> Profile | None:
        """
        Each **Concrete Iterator** class has its own implementation of the
        common **Iterator** interface.
        """
        if self.has_more():
            result = self.cache[self.current_position]
            self.current_position += 1
            return result

    def has_more(self) -> bool:
        self.lazy_init()
        return self.current_position < len(self.cache)
