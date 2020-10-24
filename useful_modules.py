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
carrie = Animal('himera', 4, 'in green polka dot')
billy = Animal('bogl', 0, 'patterned')
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

#random. randint function
import random
print(random.randint(1, 100)) 
58
print(random.randint(100, 1000)) 
861
print(random.randint(1000, 5000)) 
3795

import random
num = random.randint(1, 10)
while True:
	print('guess the number from 1 to 10') 
	guess = input()
	i = int(guess)
	if i == num:
		print('yas!')  
		break
	elif i < num:
		print('bigger')
	elif i > num:
		print('smaller')

#random. choice
desserts = ['icecream', 'pancake', 'muffin', 'cookie','chocolate']
print(random.desserts)

#random. shuffle
#continue from random.choice
random.shuffle(desserts)
print(desserts)
['muffin', 'icecream', 'chocolate', 'cookies', 'pancake']

#sys module - exit,  stdin, stdout, version.

import sys
sys.exit()

import sys
v = sys.stdin.readline()
who is who
print(v)
who is who
#readline can have limit
v = sys.stdin.readline(5)
who i

import sys
sys.stdout.write("nindzia karate navaliaye tebe")
#number of symbols will be added in the end of the line

import sys
print(sys.version)

import time
print(time.time())
#amount of second from jan 1st 1970

def lots_of_numbers(max):
              for x in range(0, max):
				print(x)

lots_of_numbers(1000)


def lots_of_numbers(max): 
		t1 = time.time()
		for x in range(0, max):
			print(x)
		t2 = time.time()
		print(' %s seconds passed' % (t2-t1))

lots_of_numbers(100)
 5.09859108925 seconds passed

#asctime
import time
print(time.asctime()) 
Thu Oct 22 23:58:46 2020

t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)

import time
t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)  
print(time.asctime(t))
