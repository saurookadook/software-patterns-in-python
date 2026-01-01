# Bridge

[_Refactoring Guru: Bridge_](https://refactoring.guru/design-patterns/bridge)

- a structural design pattern
- allows for splitting large class _(or a set of closely related classes)_ into two separate hierarchies – abstraction and implementation – which can be developed independently of each other

## The Pattern

- switches from inheritance to object composition
- extract one of dimensions into separate class hierarchy
    - means that original classes will reference object of new hierarchy instead of having all of its state and behaviors within one class

## Structure

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    Client --> Abstraction : Association
    Abstraction --o RefinedAbstraction : Aggregation
    Abstraction *-- Implementation : Composition
    Implementation <.. ConcreteImplementations : Dependency

note for Client "abstraction.feature1()"
class Client {
    <<---- Step 5 ---->>
}

note for Abstraction "// from +feature1()
i.method1()
&nbsp;
// from +feature2()
i.method2()
i.method3()"
class Abstraction {
    <<---- Step 1 ---->>
    -i: Implementation
    +feature1()
    +feature2()
}

class Implementation{
    <<---- Step 2 ---->>
    <<interface>>
    +method1()
    +method2()
    +method3()
}

namespace Bridge {
    class Abstraction
    class Implementation
}

note for RefinedAbstraction "// from +featureN()
i.methodN()
i.methodM()
i.methodL()"
class RefinedAbstraction {
    <<---- Step 4 ---->>
    +featureN()
}

class ConcreteImplementations {
    <<---- Step 3 ---->>
}
```

## Pseudocode

- illustrates how `Bridge` pattern can help divide monolithic code of an app that manages devices and their remote controls

<figure>

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    Client --> Remote : Association
    Remote --o AdvancedRemote : Aggregation
    Remote *-- Device : Composition
    Device <.. Radio : Dependency
    Device <.. TV : Dependency

note for Client "remove.togglePower()"
class Client {
    <<---- Step 5 ---->>
}

note for Remote "
if (device.isEnabled())
    device.disable()
else
    device.enable()
&nbsp;
// from +channelUp()
old = device.getChannel()
device.setChannel(old + 1)"
class Remote {
    <<---- Step 1 ---->>
    -device: Device
    +togglePower()
    +volumeDown()
    +volumeUp()
    +channelDown()
    +channelUp()
}

class Device{
    <<---- Step 2 ---->>
    <<interface>>
    +isEnabled()
    +enable()
    +disable()
    +getVolume()
    +setVolume(percent)
    +getChannel()
    +setChannel(channel)
}

namespace Bridge {
    class Remote
    class Device
}

note for AdvancedRemote "// from +mute()
device.setVolume(0)"
class AdvancedRemote {
    <<---- Step 4 ---->>
    +mute()
}

class Radio
class TV
```

<figcaption>The devices and remotes bridge example.</figcaption>

</figure>

- base remote control class declares reference field that links it with device object _(all remotes work with devices via general device interface)_
- can develop remote control classes independently from device classes
