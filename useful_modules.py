import turtle
t = turtle.Pen()


class Animal:
              def __init__(self, species, number_of_legs, color):
					self.species = species 
					self.number_of_legs = number_of_legs 
					self.color = color

harry = Animal('gippogriph', 6, 'pink')


import copy
harry = Animal('гиппогриф', 6, 'розовый')
harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)