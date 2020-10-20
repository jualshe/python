import turtle
t = turtle.Pen()


class Animal:
              def __init__(self, species, number_of_legs, color):
					self.species = species 
					self.number_of_legs = number_of_legs 
					self.color = color

harry = Animal('gippogriph', 6, 'pink')


import copy
harry = Animal('gippogriph', 6, 'pink')
harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)


harry = Animal('gippogriph', 6, 'pink')
carrie = Animal('himera', 4, 'in green pees') >>> billy = Animal('bogl', 0, 'patterned')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
print(more_animals[0].species)

gippogriph

print(more_animals[1].species)
himera

my_animals[0].species = 'vampire'
print(my_animals[0].species) 
vampire
print(more_animals[0].species) 
vampire