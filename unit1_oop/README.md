# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.


# README.md
## Implementation Documentation

### Application Scenario
I implemented a game-based character system to demonstrate object-oriented programming.
The design used a parent class, Player, and a child class, Soldier, that specialized it.
Modeling characters this way fit naturally with OOP: the class acted as a blueprint, and
each Player or Soldier I created was an object with its own data, such as health, stamina,
and an inventory.

### Parent Class: Player
The Player class served as the parent. It defined one class variable, damage_player, shared
across all instances. Its constructor (__init__) initialized two instance variables, health
and stamina. The display_info method printed the object's health and stamina, and I added a
take_damage method that subtracted a given amount from the object's health.

### Child Class: Soldier
The Soldier class inherited from Player, declared with `class Soldier(Player)`. Its constructor
called `super().__init__(health, stamina)` so the parent set up health and stamina, then added
two new instance variables of its own: an inventory (an empty, mutable list) and a primary_weapon.
Soldier also defined four new class variables for weapon names and a new method, add_item, which
appended an item to the inventory list. Finally, Soldier overrode the inherited display_info
method so it also printed the soldier's inventory.

### Namespace Demonstration
The demonstrate_namespaces function showed the difference between instance namespaces and the
class namespace using __dict__. Each soldier's __dict__ contained only that object's own instance
variables (health, stamina, inventory, primary_weapon). After I added a callsign attribute to one
soldier, it appeared in that object's __dict__ but not the other's, showing that an attribute added
to a single object belongs only to that object. The class namespace, Soldier.__dict__, held the
class variables and the methods rather than any instance data. Accessing weapon_rifle through the
class (Soldier.weapon_rifle) and through an object (s1.weapon_rifle) returned the same value,
because the object had no copy of its own and fell back to the class namespace.

### Copying and Memory Behavior
The demonstrate_copying function showed how the inventory list behaved in memory. The list started
empty and grew dynamically as add_item appended items to it. I then created a shallow copy with
copy() and a deep copy with deepcopy() of the same soldier. When I added a new item to the
original's inventory, the shallow copy changed too, because it shared the same list in memory as
the original. The deep copy was unaffected, because it held its own independent copy of the list.

### Student Extension
As my extension, I added the take_damage method to the Player class. It subtracted a given amount
of damage from the object's health instance variable and stored the reduced value back. Because
take_damage was defined in Player, the Soldier class inherited it and could use it as well, even
though Soldier never defined the method itself.


# Reflection
### I developed new programming skills with this assignment. These included learning how to develop a class properly, creating instance variables and class variables, developing objects and storing/displaying data from these objects, and overriding methods within classes. Additionally, the skill of developing reusable, robust, and adaptive code was developed. The above skill set was clearly illustrated in the code.

### The code I developed was very adaptable. When I created the “take_damage” extension, I only needed to write it once (in the Player Class), and it automatically transferred down to the Soldier Class. This made the code a reusable skeleton. Another developer would be able to start using this code as a base and add/extend upon it as they see fit.

### There were several obstacles I faced while completing this project. The largest obstacle was understanding the “namespace” example. I am partially unfamiliar with some of the terms that were being utilized and have not used Python in a while. I took my time, reviewed my Zybooks study materials again, and did the Code-Alongs, which allowed me to better understand not only how to do something but also why.

### While procedural programming appears to be more straightforward than object-oriented programming, I believe that OOP is slightly more complex due to its organization of program design. I tend to prefer top-down approaches when developing programs, both inside and outside of coding. However, I understand why OOP has become popular. Procedural programming organizes your program design in a top-down fashion with procedures/routines that are called linearly. On the other hand, OOP does nearly the opposite. It organizes your program design based on objects rather than procedures. By doing this, you can encapsulate an object's characteristics and behaviors within the same location, resulting in more organized and readable code.

### Overall, I believe that object-oriented programming provides developers with a structured method of maintaining their code. Due to the organized structure provided by OOP, developers can reuse, modify, and adapt existing code much faster than they would if they were using procedural programming. Therefore, OOP allows developers to efficiently utilize their time when developing software. In addition, because of the reusable nature of OOP, it becomes simpler for other programmers to follow the design choices that were made and continue to evolve the design further. Overall, OOP will help reduce long-term maintenance expenses by reducing duplication of effort, saving developers time, and allowing them to focus on adding value to their product.