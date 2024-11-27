# Base class
class Superhero:
    def __init__(self, name, alias, superpower, strength_level):
        self.name = name
        self.alias = alias
        self.superpower = superpower
        self.strength_level = strength_level

    def introduce(self):
        return f"I am {self.name}, also known as {self.alias}. My superpower is {self.superpower}!"

    def use_superpower(self):
        return f"{self.alias} uses {self.superpower} with a strength level of {self.strength_level}!"

# Derived class to explore polymorphism and encapsulation
class FlyingSuperhero(Superhero):
    def __init__(self, name, alias, superpower, strength_level, flight_speed):
        super().__init__(name, alias, superpower, strength_level)
        self.__flight_speed = flight_speed  # Private attribute

    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro} I can fly at a speed of {self.__flight_speed} mph!"

    def use_superpower(self):
        return f"{self.alias} uses {self.superpower} while flying at {self.__flight_speed} mph with a strength level of {self.strength_level}!"

# Creating objects
hero1 = Superhero("Clark Kent", "Superman", "Super Strength", 100)
hero2 = FlyingSuperhero("Diana Prince", "Wonder Woman", "Lasso of Truth", 90, 500)

# Using the methods
print(hero1.introduce())
print(hero1.use_superpower())
print(hero2.introduce())
print(hero2.use_superpower())
 