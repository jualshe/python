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
my_small_program = '''print('бутерброд') print('с колбасой')'''
exec(my_small_program)
