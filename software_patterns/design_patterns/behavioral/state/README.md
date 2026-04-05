# State

[_Refactoring Guru: State_](https://refactoring.guru/design-patterns/state)

_Also known as: **TBD**_

- a behavioral design pattern
- lets an object alter its behavior when its internal state changes _(appears as if object changed its class)_

## The Pattern

- closely related to concept of a _[Finite-State Machine](https://en.wikipedia.org/wiki/Finite-state_machine)_
- main idea:
    - at any given moment, there's a _finite_ number of _states_ which a program can be in
    - within any unique state, program behaves differently
    - program can be switched from one state to another instantaneously
    - however depending on current state, program may or may not switch to certain other states
    - these switching rules, called _transitions_, are also finite and predetermined
- can also apply this approach to objects
    - imagine a `Document` class
    - `Document` can be in one of three states: `Draft`, `Moderation`, or `Published`
    - the `publish` method of `Document` works differently in each state:
        - in `Draft`, moves `Document` to `Moderation`
        - in `Moderation`, makes `Document` public but only if the current user is an administrator
        - in `Published`, doesn't do anything at all

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    direction TB
    Document o-- State : Aggregation
    Draft ..|> State : Realization

    note for Document "// from +render()
    state.render()"
    class Document {
        -state
        +render()
        +publish()
        +changeState(state)
    }

    class State {
        <<interface>>
        +render()
        +publish()
    }


    note for Draft "// from +render()
    **if** (user.isAdmin **or** user.isAuthor) {
    &nbsp;&nbsp;// Render the document
    } **else** {
    &nbsp;&nbsp;// Show an error message.
    }
    "
    note for Draft "// from +publish()
    **if** (user.isAdmin) {
    &nbsp;&nbsp;document.changeState(**new** Published(document))
    } **else** {
    &nbsp;&nbsp;document.changeState(**new** Moderation(document))
    }
    "
    class Draft {
        -document
        +render()
        +publish()
    }
```

> **NOTE**: one key difference from **Strategy** pattern: in **State** pattern, the particular **States** may be aware of each other and initiate _transitions_ from one **State** to another _(whereas **Strategies** almost never know about each other)_

## Structure

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    direction BT
    Context o-- State : Aggregation
    Client --> Context : Association
    ConcreteState ..|> State : Realization
    ConcreteState --> Context : Association
    Client ..> ConcreteState : Dependency

    note for Context "// from +Context(initialState)
    **this**.state = initialState
    state.setContext(**this**)"

    note for Context "// from +doThis()
    state.doThis()"
    class Context {
        <<---- Step 1 ---->>
        -state
        +Context(initialState)
        +changeState(state)
        +doThis()
        +doThat()
    }

    class State {
        <<---- Step 2 ---->>
        <<interface>>
        +doThis()
        +doThat()
    }

    note for ConcreteState "<<---- Step 4 ---->>
    // from +doThat()
    // A state may issue state
    // transition in context
    state = **new** OtherState()
    context.changeState(state)
    "
    class ConcreteState {
        <<---- Step 3 ---->>
        <<multiple>>
        -context
        +doThis()
        +doThat()
    }

    note for Client "initialState = **new** ConcreteState()
    context = **new** Context(initialState)
    context.doThis()"
    class Client {}
```

1. **Context** stores reference to one of the **ConcreteState** objects and delegates all state-specific work to it. It also:
    - communicates with **State** object via **State** interface
    - exposes setter for passing it to new **State** object
2. **State** interface declares **State**-specific methods, which should make sense for _**all**_ **ConcreteStates** because you don't want some **States** to have useless methods that never get called.
3. **ConcreteStates** provide own implementation for the **State**-specific methods. To avoid duplication of similar code across multiple **States**, you may provide intermediate abstract classes that encapsulate some common behavior.
    - **State** objects may store backreference to **Context** object, through which the **State** can fetch any required info from **Context** as well as initiate **State** _transitions_.
4. Both **Context** and **ConcreteStates** can set next **State** of **Context** and perform actual **State** _transition_ by replacing **State** object linked to the **Context**.

## Pseudocode

<figure>

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    direction LR
    Player o-- State : Aggregation
    ReadyState --|> State : Inheritance
    LockedState --|> State : Inheritance
    PlayingState --|> State : Inheritance

    class Player {
        -state
        +UI
        +currentSong
        +playlist
        +volume

    }

    class State {
        -player
        +State(player)
        +clickLock()
        +clickPlay()
        +clickNext()
        +clickPrevious()
    }

    class ReadyState {}

    class LockedState {}

    class PlayingState {}

```

<figcaption>

**State** pattern lets same controls of the media player behave differently, depending on the current playback **State**.

</figcaption>

</figure>
