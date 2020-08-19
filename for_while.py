for x in range(0, 5):
print('hello')

#______________________
print(list(range(10, 20)))

#______________________
for x in range(0, 5):
	print('hi %s count' %x)



#______________________
>> x = 0
>>> print('hi there %s' % x) 
hi there 0
>>> x = 1
>>> print('hi there %s' % x) 
hi there 1
>>> x = 2
>>> print('hi there %s' % x) 
hi there 2
>>> x = 3
>>> print('hi there %s' % x) 
hi there 3
>>> x = 4
>>> print('hi there %s' % x) 
hi there 4


#______________________
wizard_list = ['pew1', 'pew2', 'pew3', 'pew4', 'ololo', 'looking']
    for i in wizard_list:
    	print(i)

 #without for
wizard_list = ['pew1', 'pew2', 'pew3', 'pew4', 'ololo', 'looking']
print(wizard_list[0])
pew1
print(wizard_list[1])
pew2
print(wizard_list[2])
pew3
print(wizard_list[3])
pew4
print(wizard_list[4])
ololo
print(wizard_list[5])
looking


h=[1,2,3]
 for i in h:
	print(i)
	print(i)
	print(i)
1
1
1
2
2
2
3
3
3

for i in h:
	print(i)
	for j in h:
		print(j)

1
1
2
3
2
1
2
3
3
1
2
3
