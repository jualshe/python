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


guess_this_number = 61
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
	print('you lost!')
else:
	print('you won!')

#range
for x in range(0, 5):
              print(x)

print(list(range(0, 5)))
[0, 1, 2, 3, 4]


count_by_twos = list(range(0, 30, 2))
print(count_by_twos)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

count_down_by_twos = list(range(40, 10, -2))
print(count_down_by_twos)
[40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12]


#sum
my_list_of_numbers = list(range(0, 500, 50))
print(my_list_of_numbers)
[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
print(sum(my_list_of_numbers))
2250

#working with files - open
test_file = open('/Users/julia/Documents/GitHub/python/test1.txt','w')
test_file.write('this is a test filik')
test_file.close()
print(test_file.read())


some = 'this if the way you are bad it suits you read for something encryption has gone important not messages so'
dir(some)
help(some)

some = 'this if the way you are bad it suits you read for something encryption has gone important not messages so'
x = some.split()
print (x [1::2]) # every other item after the second






