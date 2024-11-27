# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses should implement this!")

# Derived classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

class Bicycle(Vehicle):
    def move(self):
        return "Cycling 🚴"

# Creating objects
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Demonstrating polymorphism
vehicles = [car, plane, boat, bicycle]

for vehicle in vehicles:
    print(vehicle.move())
