"""
Movable Objects Demonstration
Author: SNN
Unique ID: DNN18011960  <- Watermark Here!

Week 5 Assignment 2: Polymorphism Challenge (Movable Objects)

Description:
- Defines a base class 'Movements:' with an abstract move() method.
- Implements two subclasses: Animal and NonLiving, each overriding move() differently.
- Uses 5 examples of animals: Man, Dog, Cat, Crocodile, Bird.
- Uses 5 examples of non-living objects: Car, Train, Plane, Ship, Drones.
- Saves the movement details to a CSV file in the "data" folder as 'movable_ojects.csv'.
"""

import os
import csv

def ensure_data_folder():
    """Ensure that the 'data' folder exists."""
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Created 'data' folder.")

class Movements:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method.")

# Animal subclass
class Animal(Movements):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        movement_actions = {
            "Man": "walks upright on two legs",
            "Dog": "runs swiftly on four legs",
            "Cat": "moves gracefully and silently",
            "Crocodile": "swims powerfully in water",
            "Bird": "flies high in the sky"
        }
        return movement_actions.get(self.name, "moves in its own unique way")

# NonLiving subclass
class NonLiving(Movements):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        movement_actions = {
            "Car": "drives on the road",
            "Train": "runs along the tracks",
            "Plane": "soars through the air",
            "Ship": "sails on the water",
            "Drones": "hovers and flies autonomously"
        }
        return movement_actions.get(self.name, "moves mechanically")

def save_movable_objects_to_csv(movers, filename="data/movable_ojects.csv"):
    """Save the list of movable objects to a CSV file in the data folder."""
    ensure_data_folder()
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["Category", "Name", "Movement"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for mover in movers:
            category = "Animal" if isinstance(mover, Animal) else "NonLiving"
            writer.writerow({
                "Category": category,
                "Name": mover.name,
                "Movement": mover.move()
            })

def main():
    # Create 5 animal instances
    animals = [
        Animal("Man"),
        Animal("Dog"),
        Animal("Cat"),
        Animal("Crocodile"),
        Animal("Bird")
    ]

    # Create 5 non-living object instances
    non_livings = [
        NonLiving("Car"),
        NonLiving("Train"),
        NonLiving("Plane"),
        NonLiving("Ship"),
        NonLiving("Drones")
    ]

    movers = animals + non_livings

    # Demonstrate polymorphism by printing each object's movement
    for mover in movers:
        category = "Animal" if isinstance(mover, Animal) else "NonLiving"
        print(f"{category}: '{mover.name}' {mover.move()}.")

    # Save the movement details to a CSV file
    save_movable_objects_to_csv(movers)
    print("Movable objects data saved to 'data/movable_ojects.csv'.")

if __name__ == "__main__":
    main()
