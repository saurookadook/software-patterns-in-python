# Flyweight

[_Refactoring Guru: Flyweight_](https://refactoring.guru/design-patterns/flyweight)

_Also known as: **Cache**_

- a structural design pattern
- allows for fitting more objects into available amount of RAM by sharing common parts of state between multiple objects instead of keeping all data in each object

## The Problem

To have some fun after long working hours, you decided to create a simple video game: players would be moving around a map and shooting each other. You chose to implement a realistic particle system and make it a distinctive feature of the game. Vast quantities of bullets, missiles, and shrapnel from explosions should fly all over the map and deliver a thrilling experience to the player.

Upon its completion, you pushed the last commit, built the game and sent it to your friend for a test drive. Although the game was running flawlessly on your machine, your friend wasn’t able to play for long. On his computer, the game kept crashing after a few minutes of gameplay. After spending several hours digging through debug logs, you discovered that the game crashed because of an insufficient amount of RAM. It turned out that your friend’s rig was much less powerful than your own computer, and that’s why the problem emerged so quickly on his machine.

The actual problem was related to your particle system. Each particle, such as a bullet, a missile or a piece of shrapnel was represented by a separate object containing plenty of data. At some point, when the carnage on a player’s screen reached its climax, newly created particles no longer fit into the remaining RAM, so the program crashed.

<figure>

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram
    direction LR
    Game o-- Particle : Aggregation
    Unit --> Game : Association
    Unit --> Particle : Association

note for Game "// from +draw(canvas)
&nbsp;
foreach (p in particles)
&nbsp;&nbsp;&nbsp;&nbsp;p.draw(canvas)
"
class Game {
    -particles: Particle[]
    +addParticle(particle)
    +draw(canvas)
}

note for Unit "// from +fireAt(target: Unit)
&nbsp;
p = new Particle()
p.coords = coords
p.vector = target.coords
p.speed = weaponPower
p.color = 'red'
p.sprite = load('bullet.jpeg')
Game.addParticle(p)
"
class Unit {
    +fireAt(target: Unit)
}

class Particle {
    -coords
    -vector
    -speed
    -color
    -sprite
    +move()
    +draw(canvas)
}

note "**RAM cost**
&nbsp;
coords: 8B
vector: 16B
speed: 4B
color: 4B
sprite: 20KB

--------

Particle ≈ 21KB x 1,000,000

--------

**21 GB**
"
```

<figcaption>Problem involving memory problems from particle objects in a game program.</figcaption>

</figure>

## The Solution

On closer inspection of the `Particle` class, you may notice that the color and sprite fields consume a lot more memory than other fields. What’s worse is that these two fields store almost identical data across all particles. For example, all bullets have the same color and sprite.

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram
    direction LR
    OriginalParticle ..|> MovingParticle : Realization (Refactor)
    MovingParticle "Lots" --|> "Few" Particle : Inheritance

class OriginalParticle {
    -coords
    -vector
    -speed
    -color
    -sprite
    +move()
    +draw(canvas)
}

note for MovingParticle "// for +move()
&nbsp;
particle.move(coords, vector, speed)"
note for MovingParticle "// for +draw(canvas)
&nbsp;
particle.draw(coords, canvas)"
class MovingParticle {
    <<Unique (extrinsic) state (mutable)>>
    -particle
    -coords
    -vector
    -speed
    +MovingParticle(...)
    +move()
    +draw(canvas)
}

class Particle {
    <<Repeating (intrinsic) state (immutable)>>
    -color
    -sprite
    +Particle(color, sprite)
    +move(coords, vector, speed)
    +draw(coords, canvas)
}
```

Other parts of a particle’s state, such as coordinates, movement vector and speed, are unique to each particle. After all, the values of these fields change over time. This data represents the always changing context in which the particle exists, while the color and sprite remain constant for each particle.

This constant data of an object is usually called the _**intrinsic state**_. It lives within the object; other objects can only read it, not change it. The rest of the object’s state, often altered “from the outside” by other objects, is called the _**extrinsic state**_.

The Flyweight pattern suggests that you stop storing the extrinsic state inside the object. Instead, you should pass this state to specific methods which rely on it. Only the intrinsic state stays within the object, letting you reuse it in different contexts. As a result, you’d need fewer of these objects since they only differ in the intrinsic state, which has much fewer variations than the extrinsic.

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram
    direction TB
    Game <-- Unit : Association
    Game o-- Particle : Aggregation
    Game o-- MovingParticle : Aggregation
    MovingParticle --> Particle : Association

class Game {
    -particles: Particle[]
    +addParticle(particle)
    +draw(canvas)
}

class Unit {
    +fireAt(target: Unit)
}

class Particle {
    <<Repeating (intrinsic) state (immutable)>>
    -color
    -sprite
    +Particle(color, sprite)
    +move(coords, vector, speed)
    +draw(coords, canvas)
}

class MovingParticle {
    <<Unique (extrinsic) state (mutable)>>
    -particle
    -coords
    -vector
    -speed
    +MovingParticle(...)
    +move()
    +draw(canvas)
}

note "**RAM cost**
&nbsp;
color: 4B
sprite: 20KB

------

Particle ≈ 21KB

&nbsp;
coords: 8B
vector: 16B
speed: 4B


------

MovingParticle ≈ 32B

--------

Particle (21KB) x 1
MovingParticle (32B) x 1,000,000

**32 MB**
"
```

### Extrinsic State Storage

Where does the extrinsic state move to? Some class should still store it, right? In most cases, it gets moved to the container object, which aggregates objects before we apply the pattern.

In our case, that’s the main `Game` object that stores all particles in the `particles` field. To move the extrinsic state into this class, you need to create several array fields for storing coordinates, vectors, and speed of each individual particle. But that’s not all. You need another array for storing references to a specific flyweight that represents a particle. These arrays must be in sync so that you can access all data of a particle using the same index.

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram
    direction LR
    Game_v0 ..|> Game_v1 : Realization (Refactor)
    Game_v1 ..|> Game : Realization (Refactor)


class Game_v0 {
    -particles: Particle[]
    +addParticle(particle)
    +draw(canvas)
}

class Game_v1 {
    -coords
    -vectors
    -speeds
    -references
    -particles: Particle[]
    +addParticle(particle)
    +draw(canvas)
}

note for Game "// for +addParticle(...)
&nbsp;
**1** - Go over the particles array and try to find an existing particle with the given color and sprite. If there's none, then create a new one.
**2** - Create a moving particle with given data and the particle object from the first step.
"
note for Game "// for +draw(canvas)
&nbsp;
**foreach** (p **in** moving_particles)
&nbsp;&nbsp;&nbsp;&nbsp;p.draw(canvas)
"
class Game {
    -moving_particles: MovingParticle[]
    -particles: Particle[]
    +addParticle(coords, vector, speed, color, sprite): Particle
    +draw(canvas)
}
```

A more elegant solution is to create a separate context class that would store the extrinsic state along with reference to the flyweight object. This approach would require having just a single array in the container class.

Wait a second! Won’t we need to have as many of these contextual objects as we had at the very beginning? Technically, yes. But the thing is, these objects are much smaller than before. The most memory-consuming fields have been moved to just a few flyweight objects. Now, a thousand small contextual objects can reuse a single heavy flyweight object instead of storing a thousand copies of its data.

### Flyweight and immutability

Since the same flyweight object can be used in different contexts, you have to make sure that its state can't be modified. A flyweight should initialize its state just once, via constructor parameters. It shouldn't expose any setters or public fields to other objects.

### Flyweight Factory

For more convenient access to various flyweights, you can create a factory method that manages a pool of existing flyweight objects. The method:

- accepts the intrinsic state of the desired flyweight from a client
- looks for an existing flyweight object matching this state
- if it was found, returns it
- if it was not found, creates a new flyweight and adds it to the pool

There are several options where this method could be placed. The most obvious place is a flyweight container. Alternatively, you could create a new factory class. Or you could make the factory method static and put it inside an actual flyweight class.

## Structure

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram
    direction RL
    FlyweightFactory o-- Flyweight : Aggregation
    Client *-- Context : Composition
    Context --> FlyweightFactory : Association
    Context --> Flyweight : Association

note for Context "// for +getFlyweight(repeatingState)
&nbsp;
**if** (cache[repeatingState] == null) {
&nbsp;&nbsp;&nbsp;&nbsp;cache[repeatingState] = **new** Flyweight(repeatingState)
}
**return** cache[repeatingState]"
class FlyweightFactory {
    <<---- Step 6 ---->>
    -cache: Flyweight[]
    +getFlyweight(repeatingState)
}

class Flyweight {
    <<---- Step 1, Step 2 ---->>
    -repeatingState
    +operation(uniqueState)
}

class Client {
    <<---- Step 5 ---->>
}

note for Context "// for +Context(...)
&nbsp;
**this**.uniqueState = uniqueState
**this**.flyweight = factory.getFlyweight(repeatingState)"

note for Context "// for +operation()
&nbsp;
<<---- Step 4 ---->>
flyweight.operation(uniqueState)"
class Context {
    <<---- Step 3 ---->>
    -uniqueState
    -flyweight
    +Context(repeatingState, uniqueState)
    +operation()
}
```

1. _Flyweight pattern_ is merely an optimization. Before applying it, make sure your program does have the RAM consumption problem related to having a massive number of similar objects in memory at the same time. Make sure that this problem can't be solved in any other meaningful way.
2. **Flyweight** class contains the portion of the original object's state that can be shared between multiple objects. The same **Flyweight** object can be used in many different contexts. The state stored inside a **Flyweight** is called _**intrinsic**_. The state passed to the **Flyweight's** methods is called _**extrinsic**_.
3. **Context** class contains _**extrinsic**_ state, unique across all original objects. When a context is paired with one of the **Flyweight** objects, it represents the full state of the original object.
4. Usually, the behavior of the original object remains in the **Flyweight** class. In this case, whoever calls a **Flyweight's** method must also pass appropriate bits of the _**extrinsic**_ state into the method's parameters. On the other hand, the behavior can be moved to the context class, which would use the linked **Flyweight** merely as a data object.
5. **Client** calculates or stores the _**extrinsic**_ state of **Flyweights**. From the client's perspective, a **Flyweight** is a template object which can be configured at runtime by passing some contextual data into parameters of its methods.
6. **Flyweight Factory** manages a pool of existing **Flyweights**. With the factory, clients don't create **Flyweights** directly. Instead, they call the factory, passing it bits of the _**intrinsic**_ state of the desired **Flyweight**. The factory looks over previously created **Flyweights** and either returns an existing one that matches search criteria or creates a new one if nothing is found.

## Pseudocode

<figure>

```mermaid
---
config:
    class:
        hideEmptyMembersBox: true
---
classDiagram
    direction TD
    Forest --> TreeFactory : Association
    TreeFactory *-- TreeType : Composition
    Tree --> TreeType : Association
    Forest o-- Tree : Aggregation
    %% FlyweightFactory o-- Flyweight : Aggregation

    class Forest {
        +trees: Tree[]
        +plantTree(x, y, name, color, texture): Tree
        +draw(canvas)
    }

    class TreeFactory {
        -treeTypes: TreeType[]
        +getTreeType(name, color, texture)
    }

    class TreeType {
        -name
        -color
        -texture
        +TreeType(name, color, texture)
        +draw(canvas, x, y)
    }

    class Tree {
        +x
        +y
        +type: TreeType
        +draw(canvas)
    }
```

<figcaption>

**Example**: using the **Flyweight** pattern to help reduce memory usage when rendering millions of tree objects on a canvas.

</figcaption>

</figure>

The pattern extracts repeating intrinsic state from a main `Tree` class and moves it into the **Flyweight** class `TreeType`. This means that instead of storing the same data in multiple objects, it's kept in just a few **Flyweight** objects and linked to appropriate `Tree` objects which acts as contexts.
