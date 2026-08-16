"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable. - done
# - Include at least two instance variables. - done
# - Include a constructor (__init__). - done
# - Include a method that returns or displays information about the object. - done
#
# Replace the pass statement with your implementation. - done

class Player: #Parent class
    damage_player = 5 #Class variable

    def __init__(self, health: int, stamina: float): #Initialize constructor
        self.health = health #Instance variable
        self.stamina = stamina #Instance variable

    def display_info(self): #Display info method
        print(f"Your Health is: {self.health}, Stamina is: {self.stamina:.2f}") #Makes the method print the instance variables

    def take_damage(self, damage): #Creates a new take damage method (my extension)
        self.health -= damage #Subtracts damage from the health object then stores it back into the health object with the new value


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance. - done
# - Add at least one new class variable. - done
# - Add at least two new instance variables. - done
# - Add at least one new method. - done
# - Override a method from the parent class. - done
#
# Replace the pass statement with your implementation. - done

class Soldier(Player): #Child class that inherits from the parent class
    weapon_rifle = 'M4A1' #New class variable
    weapon_pistol = 'G17' #New class variable
    weapon_sniper = '.50 Cal' #New class variable
    weapon_shotgun = 'Model 1887' #New class variable

    def __init__(self, health, stamina): #Initialize the Soldier class constructor passes health and stamina up to the parent constructor
        super().__init__(health, stamina) #
        self.inventory = [] #Creates a new instance variable
        self.primary_weapon = "M4A1" #Creates a new instance variable on the child class Soldier

    def display_info(self): #Overrides the display info method in the parent class
        print(f"Your Health is: {self.health}, Stamina is: {self.stamina:.2f}\n Weapons in your inventory: {self.inventory}") #Prints the new override

    def add_item(self, item): #Creates a new method called add_item
        self.inventory.append(item) #Appends the item to the existing inventory list


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class. - done
# - Access a class variable through the class itself. - done
# - Access the same class variable through an object. - done
# - Add a new attribute to only one object after it is created. - done
# - Display each object's namespace using __dict__. - done
# - Display information about the class namespace. - done

def demonstrate_namespaces(): #Creates a namespace
    print("\n=== Namespace Demonstration ===") #Print

    s1 = Soldier(health=250, stamina=120.0) #Sets soldier 1's health and stamina values
    s1.callsign = "Death Dealer 6" #Adds a new attribute (callsign) to the s1 object only

    s2 = Soldier(health=150, stamina=90.0) #Sets soldier 2's health and stamina values

    print("via the class", Soldier.weapon_rifle) #Accesses the class variable through the class itself
    print("via the object", s1.weapon_rifle) #Accesses the same class variable through the object
    print("s1 namespace:", s1.__dict__) #Prints soldier 1's dictionary
    print("s2 namespace:", s2.__dict__) #Prints soldier 2's dictionary
    print("Class namespace:", Soldier.__dict__) #Prints class Soldier dictionary


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying(): #Copy method
    print("\n=== Copy Demonstration ===") #Print

    #Original
    original = Soldier(health=250, stamina=120.0)
    original.add_item("M4A1") #Adds the item to the original inventory list
    original.add_item("G17") #Adds the item to the original inventory list

    #Shallow & Deep Copy
    shallow = copy(original) #Makes a new copy of Soldier, but shares the original inventory list
    deep = deepcopy(original) #Makes a new (deep) copy of Soldier, but with a new and fresh inventory list

    #Adds a new item to the original list, thus adding it to the shallow copy list as well, but not the deep copy list
    original.add_item("Grenade") #Adds a new item to the original inventory list

    #Print
    print(f"Original Inventory: {original.inventory}") #Prints the original inventory list
    print(f"Shallow copy of Inventory: {shallow.inventory}") #Prints the shallow copy (the same list as the inventory)
    print(f"Deep copy of Inventory: {deep.inventory}") #Prints the deep copy (an individual list itself, not a copy of the inventory list)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class. - done
# - Create at least one object from the child class. - done
# - Demonstrate inheritance by calling methods. - done
# - Call your namespace demonstration function. - done
# - Call your copy demonstration function. - done

def main(): #Defines the main function
    print("=== Unit 1 OOP Assignment ===") #Print

    #Player (parent) create and call the method display info
    p = Player(health=250, stamina=120.0) #Sets the health and stamina values for class Player
    p.take_damage(75) #Deals damage to the player
    p.display_info() #Calls the display info method in class Player

    #Soldier (child) create and call the method display info overriding the parents display info method
    s = Soldier(health=250, stamina=120.0) #Sets the health and stamina values for class Soldier
    s.take_damage(20) #Deals damage to the soldier
    s.add_item("M4A1") #Adds the item to the soldier's inventory
    s.display_info() #Calls the display info method in class Soldier (overriding the display info method in class Player)

    demonstrate_namespaces() #
    demonstrate_copying() #


if __name__ == "__main__": #Runs main() only when this file is run directly
    main() #Runs the main function