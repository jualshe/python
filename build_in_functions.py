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