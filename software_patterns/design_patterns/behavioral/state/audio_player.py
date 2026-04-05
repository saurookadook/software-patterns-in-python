from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

from .concrete_states import LockedState, PlayingState, ReadyState

if TYPE_CHECKING:
    from .state_interface import State


class Element:
    def on_click(self, func: Callable[[], None]) -> None:
        func()


class UserInterface:

    def __init__(self) -> None:
        self.lock_button: Element = Element()
        self.play_button: Element = Element()
        self.next_button: Element = Element()
        self.previous_button: Element = Element()


class AudioPlayer:
    """
    The ``AudioPlayer`` class acts as a ``Context``. It also maintains a
    reference to an instance of one of the ``State`` classes that represents
    the current ``State`` of the ``AudioPlayer``.
    """

    state: State
    UI: UserInterface
    current_song: Any
    is_playing: bool
    playlist: list[Any]
    volume: float

    def __init__(self) -> None:
        """
        ``Context`` delegates handling user input to a ``State`` object.
        Naturally, the outcome depends on what ``State`` is currently active,
        since each ``State`` can handle input differently.
        """
        self.state = ReadyState(self)

        self.UI = UserInterface()
        self.UI.lock_button.on_click(self.click_lock)
        self.UI.play_button.on_click(self.click_play)
        self.UI.next_button.on_click(self.click_next)
        self.UI.previous_button.on_click(self.click_previous)

        self.current_song = None
        self.is_playing = False
        self.playlist = []
        self.volume = 0.5

    def change_state(self, state: State) -> None:
        """
        Other objects must be able to switch the ``AudioPlayer``'s active state.
        """
        self.state = state

    # UI Methods delegate execution to the active state
    def click_lock(self) -> None:
        self.state.click_lock()

    def click_play(self) -> None:
        self.state.click_play()

    def click_next(self) -> None:
        self.state.click_next()

    def click_previous(self) -> None:
        self.state.click_previous()

    # A state may call some service methods on the ``Context``.
    def start_playback(self) -> None:
        print(f"Playing {self.current_song} at volume {self.volume}")

    def stop_playback(self) -> None:
        print(f"Stopped {self.current_song}")

    def next_song(self) -> None:
        print(f"Playing next song in the playlist")

    def previous_song(self) -> None:
        print(f"Playing previous song in the playlist")

    def fast_forward(self, seconds: int) -> None:
        print(f"Fast forwarding {self.current_song} by {seconds} seconds...")

    def rewind(self, seconds: int) -> None:
        print(f"Rewinding {self.current_song} by {seconds} seconds...")
