from .interfaces import ConcreteBaseDevice


class TV(ConcreteBaseDevice):

    def set_channel(self, channel: int | float) -> None:
        channel_as_int = int(channel)
        self._channel = max(1, min(channel_as_int, 999))


class Radio(ConcreteBaseDevice):
    _volume: float = 50.0
    _channel: float = 101.1

    def set_volume(self, percent: float) -> None:
        self._volume = max(0.0, min(percent, 100.0))
