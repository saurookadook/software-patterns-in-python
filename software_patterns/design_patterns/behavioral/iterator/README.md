# Iterator

[_Refactoring Guru: Iterator_](https://refactoring.guru/design-patterns/iterator)

_Also known as: **TBD**_

- a behavioral design pattern
- lets you traverse elements of collection without exposing underlying representation _(list, stack, tree, etc.)_

## The Pattern

- main idea: extract traversal behavior of collection into a separate object called an **Iterator**

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    TreeCollection --> DepthFirstIterator : Association
    TreeCollection --> BreadthFirstIterator : Association

    class TreeCollection {
        +getDepthIterator()
        +getBreadthIterator()
    }

    class DepthFirstIterator {
        -currentElement
        +getNext(): Element
        +hasMore(): bool
    }

    class BreadthFirstIterator {
        -currentElement
        +getNext(): Element
        +hasMore(): bool
    }
```

## Structure

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    Client --> Iterator : Association
    Client --> IterableCollection : Association
    ConcreteIterator ..|> Iterator : Realization
    IterableCollection ..> Iterator : Dependency
    ConcreteCollection ..|> IterableCollection : Realization
    ConcreteCollection <--> ConcreteIterator : Association

    class Client {
        <<---- Step 5 ---->>
        +getDepthIterator()
        +getBreadthIterator()
    }

    class Iterator {
        <<---- Step 1 ---->>
        <<interface>>
        +getNext(): Element
        +hasMore(): bool
    }

    class IterableCollection {
        <<---- Step 3 ---->>
        <<interface>>
        +createIterator(): Iterator
    }

    class ConcreteIterator {
        <<---- Step 2 ---->>
        -collection: ConcreteCollection
        -iterationState
        +ConcreteIterator(c: ConcreteCollection)
        +getNext()
        +hasMore(): bool
    }

    class ConcreteCollection {
        <<---- Step 4 ---->>
        +createIterator(): Iterator
    }

```

1. **Iterator** interface declares operations required for traversing collection:
    - fetching next element
    - retrieving current position
    - restarting iteration
    - etc.
2. **Concrete Iterators** implement specific algorithms for traversing collection
    - should track traversal progress on its own, which allows several iterators to traverse same collection independently of each other
3. **Collection** interface declares one or multiple methods for getting iterators compatible with collection
    - _**NOTE**: return type of methods must be declared as **Iterator** interface so that **Concrete Collections** can return various kinds of iterators_
4. **Concrete Collection** returns new instances of particular **Concrete Iterator** class each time client requests one
5. **Client** works with both **Collections** and **Iterators** via their interfaces, thereby decoupling it from concrete classes
    - don't typically create **Iterators** on their own, instead getting them from **Collections**

## Pseudocode

<figure>

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    SocialSpammer ..> Profile : Dependency
    SocialSpammer --> ProfileIterator : Association
    ProfileIterator <|.. FacebookIterator : Realization
    Application --> SocialSpammer : Association
    SocialNetwork ..> ProfileIterator : Dependency
    Facebook <--> FacebookIterator : Association
    Facebook ..|> SocialNetwork : Realization
    Facebook *-- Profile : Composition
    Application --> Facebook : Association

    class SocialSpammer {
        +send(iterator, message)
    }

    class Application {
        -spammer
        -network
        +sendSpamToFriend(profile)
        +sendSpamToCoworker(profile)
    }

    class Profile {
        +getId()
        +getEmail()
    }

    class ProfileIterator {
        <<interface>>
        +getNext(): Profile
        +hasMore(): bool
    }

    class SocialNetwork {
        <<interface>>
        +createFriendsIterator(profileId): ProfileIterator
        +createCoworkersIterator(profileId): ProfileIterator
    }

    class FacebookIterator {
        -facebook: Facebook
        -profileId
        -type
        -currentPosition
        -cache: Profile[]
        +FacebookIterator(...)
        -lazyInit()
        +getNext(): Profile
        +hasMore(): bool
    }

    class Facebook {
        +createFriendsIterator(profileId): ProfileIterator
        +createCoworkersIterator(profileId): ProfileIterator
    }
```

<figcaption>

**Iterator** pattern is used to walk through a special kind of **Collection** which encapsulates access to Facebook's social graph. The **Collection** provides several **Iterators** that can traverse profiles in various ways.

</figcaption>

</figure>
