from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .event_listener_interface import EventListener

EventType = str


class EventManager:
    """
    The base **Publisher** class includes subscription management code
    and notification methods.
    """

    listeners: dict[EventType, list[EventListener]]

    def __init__(self) -> None:
        self.listeners = defaultdict(list)

    def subscribe(self, event_type: EventType, listener: EventListener) -> None:
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type: EventType, listener: EventListener) -> None:
        self.listeners[event_type].remove(listener)

    def notify(self, event_type: EventType, data: Any) -> None:
        for listener in self.listeners[event_type]:
            listener.update(data)
