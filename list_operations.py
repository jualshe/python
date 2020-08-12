#append

stooges.append('Shemp')

#<list>+<list>

[0,1]+[2,3] -> [0,1,2,3]

#del(<list>)[element]

#len(<list>)
len([0,1]) ->2
len(['a',['b',['c']]]) ->2
len("ababagalamaga") -> 13

#quiz 
p = [1,2]
p.append(3)
p = p + [4,5]
print len(p)
->5


#quiz2

p =[1,2]
q = [3,4]
p.append(q)
print len(p)

->3 
#print p
#[1, 2, [3, 4]]