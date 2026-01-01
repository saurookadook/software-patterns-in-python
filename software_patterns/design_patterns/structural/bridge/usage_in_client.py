from __future__ import annotations

from .devices import TV, Radio
from .remote_control import ReomteControl, AdvancedRemoteControl


def run():
    tv = TV()
    remote = AdvancedRemoteControl(tv)
    remote.toggle_power()

    radio = Radio()
    remote = ReomteControl(radio)
    remote.toggle_power()


if __name__ == "__main__":
    run()
