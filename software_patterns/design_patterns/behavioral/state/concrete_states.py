"""
``ConcreteStates`` implement various behaviors associated with
a ``State`` of the ``Context``.
"""

from __future__ import annotations

from typing import Any, override

from .state_interface import State


class LockedState(State):
    def click_lock(self) -> None:
        """
        When you unlock a locked player, it may assume one of two ``States``.
        """
        if self.player.is_playing:
            self.player.change_state(PlayingState(self.player))
        else:
            self.player.change_state(ReadyState(self.player))

    def click_play(self) -> None:
        pass

    def click_next(self) -> None:
        pass

    def click_previous(self) -> None:
        pass


class ReadyState(State):
    def click_lock(self) -> None:
        self.player.change_state(LockedState(self.player))

    def click_play(self) -> None:
        self.player.start_playback()
        self.player.change_state(PlayingState(self.player))

    def click_next(self) -> None:
        self.player.next_song()

    def click_previous(self) -> None:
        self.player.previous_song()


class PlayingState(State):
    def click_lock(self) -> None:
        self.player.change_state(LockedState(self.player))

    def click_play(self) -> None:
        self.player.stop_playback()
        self.player.change_state(ReadyState(self.player))

    @override
    def click_next(self, event: Any) -> None:  # type: ignore
        if event.double_click:
            self.player.next_song()
        else:
            self.player.fast_forward(5)

    @override
    def click_previous(self, event: Any) -> None:  # type: ignore
        if event.double_click:
            self.player.previous_song()
        else:
            self.player.rewind(5)
