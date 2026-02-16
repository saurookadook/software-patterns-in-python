from __future__ import annotations

from .component import Component
from .mediator_interface import Mediator


class AuthenticationDialog(Mediator):
    """The concrete mediator class. The intertwined web of connections between
    individual components has been untangled and moved into the mediator.

    Create all component objects by passing the current mediator into their
    constructors to establish links
    """

    def __init__(self) -> None:
        self.title = "Authentication"
        self.login_or_register_checkbox = None
        self.login_username = None
        self.login_password = None
        self.registration_username = None
        self.registration_password = None
        self.registration_email = None
        self.ok_button = None
        self.cancel_button = None

    def notify(self, sender: Component, event: str) -> None:
        """When something happens with a component, it notifies the mediator.
        Upon receiving a notification, the mediator may do something on its
        own or pass the request to another component.
        """

        if sender == self.login_or_register_checkbox and event == "check":
            if self.login_or_register_checkbox.checked:
                self.title = "Log In"
                # 1. Show login form components
                # 2. Hide registration form components
            else:
                self.title = "Register"
                # 1. Show registration form components
                # 2. Hide login form components

        if sender == self.ok_button and event == "click":
            if self.login_or_register_checkbox.checked:
                # Try to find a user using login credentials
                if not self.found:
                    # Show an error message above login field
                    pass
            else:
                # 1. Create a user account using data from the registration fields
                # 2. Log that user in
                # ...
                pass
