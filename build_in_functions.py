#abs
print(abs(10)) 
print(abs(-10))

steps = -3
if abs(steps) > 0:
	print('Character moves')

#bool
print(bool(0))
>>>False
print(bool(1))
print(bool(1123.23))
print(bool(-500))

print(bool(None))
>>>False
print(bool('a'))
print(bool(' '))
print(bool('What do you call bears with no ears? B.'))

my_silly_list = []
print(bool(my_silly_list))
>>>False
my_silly_list = ['s', 'i', 'l', 'l', 'y']
print(bool(my_silly_list))
>>>True

year = input('Year of birth: ')
if not bool(year.rstrip()):
              print('enter the year')

#dir  - what functions can be used 
dir(['this is', 'short', 'list'])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__',
'__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

dir(1)

popcorn = 'I like popcorn!'
dir(popcorn)
help(popcorn.upper)


#eval
#if call eval('print("wow!")') - > print("wow!") will be executed
eval('10*5')
50
#this not gonna work
eval('''if True:
print("it's not gonna work")''')

your_calculation = input('enter expression: ')
12*52
eval(your_calculation)
print(your_calculation)

#exec
my_small_program = '''print('sandwich') print('with ham')'''
exec(my_small_program)

#float
float('12')
12.0

float('123.456789') 
123.456789

your_age = input('enter you age: ')
age = float(your_age)
if age > 13:
print('you are %s years older, than needed' % (age - 13))

#int
int(123.456)
123

#len
>>> len('1234567890')
10

creature_list = ['dino', 'mighty', 'colly', 'sabazun', 'mokriy piven']
print(len(creature_list))
5

enemies_map = { 'batman':'joker',
	'superman':'lex lutor',
	'spiderman':'green goblin'}
len(enemies_map)
3


fruit = ['apple', 'banana', 'mandarin', 'papaya'] 
length = len(fruit)
for x in range(0, length):
	print('fruit with an index %s: %s' % (x, fruit[x]))


#max and min
numbers = [5, 4, 10, 30, 22]
print(max(numbers))
30

string='chipucheka'
print(max(string))

print(max(10, 300, 450, 50, 90))
      

numbers = [5, 4, 10, 30, 22]
print(min(numbers))