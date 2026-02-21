# Memento

[_Refactoring Guru: Memento_](https://refactoring.guru/design-patterns/memento)

## The Pattern

- a behavioral design pattern
- allows for saving and restoring previous state of an object without revealing details of its implementation

## Structure

### Implementation based on nested classes

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    direction LR
    Originator ..> Memento : Dependency
    Memento --o Caretaker : Aggregation

    note for History "<<---- Step 4 (History) ---->>"
    namespace History {
        class Originator {
            <<---- Step 1 ---->>
            -state
            +save(): Memento
            +restore(m: Memento)
        }

        class Memento {
            <<---- Step 2 ---->>
            -state
            -Memento()
            -getState()
        }
    }

    class Caretaker {
        <<---- Step 3 ---->>
        -originator
        -history: Memento[]
        +doSomething()
        +undo()
    }
    note for Caretaker "// from +doSomething()
    m = originator.save()
    history.push(m)
    // originator.change()"
    note for Caretaker "// from +under()
    m = history.pop()
    originator.restore(m)"

```

1. **Originator** class produces snapshots of its own state, as well as restore its state from snapshots
2. **Memento** is value object that acts as a snapshot of **Originator**'s state. Common practice is to make **Memento** immutable and pass it data only once via constructor.
3. **Caretaker** knows when and why to capture **Originator**'s state, as well as when state should be restored.
   - can keep track of **Originator**'s history by storing stack of **Mementos**
   - when **Originator** has to travel back in history, **Caretaker** fetches topmost **Memento** from stack and passes it to **Originator**'s restoration method
4. In this implementation, **Memento** class is nested inside **Originator**, which lets **Originator** access fields and methods of **Memento**, even though they're declared private. On the other hand, **Caretaker** has very limited access to **Memento**'s fields and methods, which lets it store **Mementos** in a stack without tampering with their state.

### Implementation based on intermediate interface

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    direction RL
    Memento --o Client : Aggregation
    ConcreteMemento ..|> Memento : Realization
    Originator ..> ConcreteMemento : Dependency

    class Client {
        -originator
        -history: Memento[]
        +undo()
    }

    class Memento {
        <<interface>>
    }

    class ConcreteMemento {
        <<---- Step 2 ---->>
        -state
        -ConcreteMemento()
        -getState()
    }

    class Originator {
        <<---- Step 1 ---->>
        -state
        +save(): Memento
        +restore(m: Memento)
    }
    note for Originator "// from +restore(m: Memento)
    cm = (ConcreteMemento) m
    state = cm.getState()"

```

1. In absence of nested classes, can restrict access to **Memento**'s fields by establishing a convention that **Caretakers** can work with a **Memento** _**only**_ through explicitly declared intermediary interface _(which would only declare methods related to **Memento**'s metadata)_
2. On the other hand, **Originators** can work with **Memento** object directly, accessing fields and methods declared in **Memento** class. The downside is that all members of **Memento** must be publicly declared.

### Implementation with even stricter encapsulation

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    direction RL
    Memento --o Caretaker : Aggregation
    Originator ..> Memento : Dependency
    ConcreteMemento ..|> Memento : Realization
    Originator ..|>  ConcreteOriginator : Realization
    ConcreteMemento <--> ConcreteOriginator : Association

    class Caretaker {
        -originator
        -history: Memento[]
        +undo()
    }

    class Memento {
        <<interface>>
        +restore()
    }

    note for Originator "<<---- Step 3 ---->>"
    class Originator {
        <<interface>>
        +save(): Memento
    }

    class ConcreteMemento {
        <<---- Step 3 ---->>
        -originator
        -state
        +ConcreteMemento(originator, state)
        +restore()
    }
    note for ConcreteMemento "// from +restore()
    originator.setState(state)"

    class ConcreteOriginator {
        <<---- Step 1 ---->>
        -state
        +save(): Memento
        +setState(state)
    }

```

1. This implementation allows having multiple types of **Originators** and **Mementos**. Each **Originator** works with corresponding **Memento** class. Neither **Originators** nor **Mementos** expose their state to anyone.
2. **Caretakers** now explicitly restricted from changing state stored in **Mementos**. **Caretaker** class becomes independent from **Originator** because restoration method is now defined in **Memento** class.
3. Each **Memento** becomes linked to **Originator** that produced it. **Originator** passes itself to **Memento**'s constructor, along with values of its state. Thanks to close relationship between these classes, **Memento** can restore the state of its **Originator**, given that the latter has defined the appropriate setters.

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
    Editor <--> Snapshot : Association
    Snapshot <-- Command : Association

    class Editor {
        -state
        +setState(x)
        +createSnapshot()
    }

    class Snapshot {
        -state
        +Snapshot(state)
        +restore()
    }

    class Command {
        -backup: Snapshot
        +makeBackup()
        +undo()
    }

```

<figcaption>

Saving snapshots of the text editor's state.

</figcaption>

</figure>
