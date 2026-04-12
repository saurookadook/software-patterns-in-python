from __future__ import annotations

from typing import TYPE_CHECKING

from .client import SocialSpammer
from .concrete_collection import Facebook, SocialNetwork

if TYPE_CHECKING:
    from .concrete_iterator import Profile


class Application:
    """
    The application class configures **Collections** and **Iterators** and
    then passes them to the **Client** code.
    """

    network: SocialNetwork
    spammer: SocialSpammer

    def config(self) -> None:
        if globals().get("is_working_with_facebook"):
            self.network = Facebook()
        if globals().get("is_working_with_linkedin"):
            self.network = LinkedIn()  # type: ignore
        self.spammer = SocialSpammer()

    def send_spam_to_friends(self, profile: Profile) -> None:
        iterator = self.network.create_friends_iterator(profile.profile_id)
        self.spammer.send(iterator, "Very important message!")

    def send_spam_to_coworkers(self, profile: Profile) -> None:
        iterator = self.network.create_coworkers_iterator(profile.profile_id)
        self.spammer.send(iterator, "Very important message!")
