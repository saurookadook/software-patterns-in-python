# Decorator

[_Refactoring Guru: Decorator_](https://refactoring.guru/design-patterns/decorator)

_Also known as: **Wrapper**_

- a structural design pattern
- allows for attaching new behaviors to objects by placing them inside special wrapper object that contains behaviors

## The Pattern

- object that can be linked with some _target_ object
- contains same set of methods as target and delegates to it all requests it receives
- may alter result by doing something either before or after it pass request to target

```mermaid
---
title: "Decorator example: Various notification methods become decorators."
---
classDiagram
    Notifier <|-- BaseDecorator : Inheritance
    BaseDecorator o-- Notifier : Aggregation
    BaseDecorator <|-- SMSDecorator : Inheritance
    BaseDecorator <|-- FacebookDecorator : Inheritance
    BaseDecorator <|-- SlackDecorator : Inheritance


    class Notifier{
        ...
        +send(message)
    }
    note for BaseDecorator "wrapper.send(message);"
    class BaseDecorator{
        -wrappee: Notifier
        +BaseDecorator(notifier)
        +send(message)
    }
    note for SMSDecorator "**super**::send(message);
    sendSMS(message);"
    class SMSDecorator{
        ...
        +send(message)
    }
    class FacebookDecorator{
        ...
        +send(message)
    }
    class SlackDecorator{
        ...
        +send(message)
    }
```

```mermaid
---
title: "Decorator example: Apps might configure complex stacks of notifiation decorators."
---
classDiagram
    direction RL

    note "stack = new Notifier();
    if (facebookEnabled)
        stack = new FacebookDecorator(stack)
    if (slackEnabled)
        stack = new SlackDecorator(stack)

    app.setNotifier(stack)"

    class Application{
        -notifier: Notifier
        +setNotifier(notifier)
        +doSomething()
    }
    note for Application "notifier.send('Alert!')
    // Email -> Facebook -> Slack"
```

## Structure

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    Client --|> Component : Inheritance
    Component --o BaseDecorator : Aggregation
    Component <.. ConcreteComponent : Dependency
    Component <.. BaseDecorator : Dependency
    BaseDecorator <-- ConcreteDecorators : Association

    note for Client "<<---- Step 5 ---->>
    a = new ConcreteComponent()
    b = new ConcreteComponent1(a)
    c = new ConcreteComponent2(b)
    c.execute()
    // Decorator -> Decorator -> Component"
    class Client

    class Component{
        <<---- Step 1 ---->>
        <<interface>>
        +execute()
    }
    class ConcreteComponent{
        <<---- Step 2 ---->>
        ...
        +execute()
    }
    note for BaseDecorator "// from +BaseDecorator(c: Component)
    wrappee = c"
    note for BaseDecorator "// from +execute()
    wrappee.execute()"
    class BaseDecorator{
        <<---- Step 3 ---->>
        -wrappee: Component
        +BaseDecorator(c: Component)
        +execute()
    }
    note for ConcreteDecorators "**super**::execute()
    extra()"
    class ConcreteDecorators{
        <<---- Step 4 ---->>
        ...
        +execute()
        +extra()
    }
```

1. **Component**: declares common interface for both wrappers and wrapped objects
2. **Concrete Component**: class of objects being wrapped
    - defines basic behavior which can be altered by decorators
3. **Base Decorator**: class has field for referencing a wrapped object
    - field's type should be declared as component interface so it can contain both concrete components and decorators
    - base decorator delegates all operations to wrapped object
4. **Concrete Decorators**: define extra behaviors that can be added to components dynamically
    - concrete decorators override methods of base decorator and execute their behavior before or after calling parent method
5. **Client**: can wrap components in multiple layers of decorators _(as long as it works with all objects via component interface)_

## Pseudocode

<figure>

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram

    Client --|> DataSource : Inheritance
    DataSource --o DataSourceDecorator : Aggregation
    DataSource <.. FileDataSource : Dependency
    DataSource <.. DataSourceDecorator : Dependency
    DataSourceDecorator <-- EncryptionDecorator : Association
    DataSourceDecorator <-- CompressionDecorator : Association

    class Client

    class DataSource{
        <<interface>>
        +writeData(data)
        +readData()
    }
    class FileDataSource{
        -filename
        +FileDataSource(filename)
        +writeData(data)
        +readData()
    }
    class DataSourceDecorator{
        -wrappee: DataSource
        +DataSourceDecorator(s: DataSource)
        +writeData(data)
        +readData()
    }
    class EncryptionDecorator{
        ...
        +writeData(data)
        +readData()
    }
    class CompressionDecorator{
        ...
        +writeData(data)
        +readData()
    }
```

<figcaption>The encryption and compression decorators example.</figcaption>

</figure>

- application wraps data source object with a pair of decorators
- both wrappers change way data is written and read from disk:
    - before data is written to disk, decorators encrypt and compress it _(original class writes encrypted, protected data to file without knowing about the change)_
    - right after data is read to disk, goes through same decorators which decompress and decode it
