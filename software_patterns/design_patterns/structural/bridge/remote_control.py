from __future__ import annotations

from .interfaces import Device


class ReomteControl:
    """The 'abstraction' defines the interface for the 'control'
    part of the two class hierarchies. It maintains a reference to an
    object of the 'implementation' hierarchy and delegates all of the
    real work to this object.
    """

    device: Device

    def __init__(self, device: Device) -> None:
        self.device = device

    def toggle_power(self) -> None:
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self) -> None:
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self) -> None:
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self) -> None:
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self) -> None:
        self.device.set_channel(self.device.get_channel() + 1)


class AdvancedRemoteControl(ReomteControl):
    """You can extend the abstraction without changing the
    implementation classes.
    """

    def mute(self) -> None:
        self.device.set_volume(0)
