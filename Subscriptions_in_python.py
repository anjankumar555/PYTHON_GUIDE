#SUBSCRIPTION: it selects an item of sequence object such as LIST,TUPLE,SET,DICTIONARY and FROZENSET.
#SYNTAX:identifier[indice value]

#it selects item from a sequence
#it select an item from left to right starting from indice value is 0.
#it is same rule for TUPLE,SET and  STRINGS.

#NOTE:object supports subscription by defining __getitem__() method internally.

#NOTE:INDICES VALUE 0,1,2,3,..... from left to right.

#NOTE:if indices values not found means more than items in object, it raises ERROR: List index out of range.


primary_1=[1,2,3,4,5]#sequence object created for primary_1.

#if primary object is sequence then object asked to evaluate integer as indice value.

print(primary_1[0])#it access first item in list with indice 0.
print(primary_1[1])#it access second item
print(primary_1[2])
print(primary_1[3])
print(primary_1[4])

#Reverse selection with negative value of indices.

#NOTE:INDICES VALUE -1,-2,-3,......from right to left.

print(primary_1[-1])
print(primary_1[-2])
print(primary_1[-3])
print(primary_1[-4])
print(primary_1[-5])

#NOTE:Dictionary object subscription is made by key.

#DICTIONARY object:
dict_2={'x':1,'y':2,'z':3,'X':4,'a':(1,2),1:'a'}#sequence mapping dictionary object is created for primary_2 
print(dict_2)#it returns object.
print(dict_2['x'])
print(dict_2['y'])
print(dict_2['z'])
print(dict_2['X'])
print(dict_2['a'])
print(dict_2[1])

#TUPLE object:
tuple_1=(1,2,3,4,5)#tuple object created for primary tuple_1
print(type(tuple_1))
print(tuple_1[2])
print(tuple_1[-4])
print(tuple_1[-1])
tuple_2=(1,)#tuple has only one item
print(type(tuple_2))
print(tuple_2[0])
print(tuple_2[-1])

#STRING object:
string_1='hello'
print(string_1[0])
print(string_1[1])
print(string_1[2])
print(string_1[3])
print(string_1[4])
#starting from right to left as negative indices
print(string_1[-1])
print(string_1[-2])
print(string_1[-3])
print(string_1[-4])
print(string_1[-5])

#NOTE:FROZENSET object is not subscriptable.

#FROZENSET object:
frozen_1=frozenset((1,2,3,4,5))
print(frozen_1)
