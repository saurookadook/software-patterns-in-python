# Prototype

Also known as 'clone', **prototype** is a creational design pattern that lets you copy existing objects without making code dependent on their classes.

## Basic Implementation

```txt
┏━━━━━━━━━━━━━━━━━━━━━━━┓
┃ (interface) Prototype ┃
┣━━━━━━━━━━━━━━━━━━━━━━━┫
┃ + clone(): Prototype  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━┛
           /┃\
            ┃
┏━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━┓
┃ ConcretePrototype               ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ + ConcretePrototype(prototype)  ┃
┃ + clone(): Prototype            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
           /┃\
            ┃
┏━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━┓
┃ SubclassPrototype               ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ + SubclassPrototype(prototype)  ┃
┃ + clone(): Prototype            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

1. **Prototype** interface declares cloning methods _(usually just a single `clone` method)_
2. **Concrete Prototype** class implements cloning method(s). In addition to copying original object's data to clone, this method may also handle edge cases of cloning process related to cloning linked objects, untangling recursive dependencies, etc.
