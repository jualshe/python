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

sally = Animal('sphinx', 4, 'sandy')
my_animals.append(sally)
print(len(my_animals))
4
print(len(more_animals))
3

more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'dragon'
print(my_animals[0].species)
dragon
print(more_animals[0].species)
vampire


#keyword module
import keyword
print(keyword.iskeyword('if'))
True
print(keyword.iskeyword('ozwald'))
False 
print(keyword.kwlist)

#randint function
import random
print(random.randint(1, 100)) 
58
print(random.randint(100, 1000)) 
861
print(random.randint(1000, 5000)) 
3795