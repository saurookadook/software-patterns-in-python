from __future__ import annotations

from .interfaces import ProfileIterator


class System:

    @classmethod
    def send_email(cls, email: str, message: str) -> None:
        print(f"Send email to {email} with message: {message}")


class SocialSpammer:
    """
    Here is another useful trick: you can pass an **Iterator** to a **Client**
    class instead of giving it access to a whole **Collection**. This way,
    you don't expose the **Collection** to the **Client**.

    And there's another benefit: you can change the way the **Client** works
    with the **Collection** at runtime by passing it a different **Iterator**.
    This is possible because the **Client** code isn't coupled to any
    **Concrete Iterator** classes.
    """

    def send(self, iterator: ProfileIterator, message: str) -> None:
        while iterator.has_more():
            profile = iterator.get_next()
            System.send_email(profile.email, message)  # type: ignore
