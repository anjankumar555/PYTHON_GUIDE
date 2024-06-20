#Primaries or Basics of Python programming Language.
#Primaries:these are bounding operations of language.
#Primaries:Atom,Attribute Reference,Subscription,Slicing,Call.these are most basic elements of programming language.
#1.Atom:Identifiers or Literals.
a=2_0;b=3_0#these are atoms
print(a+b)#atoms of operation.
print(10+100)#these are also Atoms.
print(a*10)#here 10 also a atom.
print((a+b*20)/2**(2%4))#grouping Atoms forms an operation.or Enclosure
print([a*b+100,a*b])
print([1,2,3,4,5])#Atoms in LIST.
print((1,2,3,4,5))#Atoms in TUPLE.
print({1,2,3,4,5})#Atoms in SET.
print({1:10,2:100,3:'a',4:'python',5:'java'})#Atoms in DICT.
print([1,2,4,5,6,8,7,9])#List or Packing.
print(*[1,2,4,5,6,8,7,9])#Unpacking by Asterisk.
print(*[1],*[2],*[1,2,3])
print(dict({'x':2,'y':4,'z':5}))
print(*(1,2,3,4,5,6))#Unpacking TUPLE
print(*{1,2,3,4,5,6})#Unpacking SET
#NOTE: * is a iterable unpacking operator and ** is a dictionary unpacking operators to allow unpacking in more positions,
#an arbitrary number of times, and in additional circumstances.Specifically, in function calls, in comprehensions and generator expressions, and in displays.
print('Expression LIST:')
print((3 if 2<3 else 0)*[1,2,4,5,6,8,7,9])#Expression List.
print((5 if 1<4 else -1)*[1,2,4,5,6,8,7,9])
print((1 if 1<4 else -1)*[1,2,4,5,6,8,7,9],(3 if 2<3 else 0)*[1,2,4,5,6,8,7,9])#Expression LIST.
print('Starred LIST:')
print((1 if 1<4 else -1),(3 if 2<3 else 0)*[1,2,4,5,6,8,7,9])#Starred LIST.
print((1 if 1<4 else -1),(3 if 2<3 else 0),(2 if 4<0 else 4)*[1,2,4,5,6,8,7,9])
print('Starred Expression:')
print((1 if 1<4 else -1),(3 if 2<3 else 0),(5 if 1<4 else -1)*[3 if 2<3 else 0])#Starred Expression.
print((1 if 1<4 else -1),(3 if 2<3 else 0),(10 if 1<4 else -1)*[3 if 2<3 else 0])#it prints 3 in LIST for 10 times.
print([x*y for x in range(10) for y in range(x,x+10)])

