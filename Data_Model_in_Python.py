#DATA MODEL IN PYTHON:
#Data Model in python defines abstraction of data. it divides 3 types
#1.OBJECT, 2.VALUE(object value) 3.TYPE(object type)

#NOTE: All data in python program is represented by Objects or relation between the Objects. Code is also represented by objects.

#Everything is an object in python and it generates next level.

#NOTE:A CLASS initiated internally when an object has been created. because object derived from the class.

#so that creating a new class creates a new type of object, allowing new instances of that type to be made.

#each class instance(object) can have attributes attached to it for Maintaining its state.

#each class instance(object) can have methods(defined by class) for Modifying its state.

print('CLASS INITIATED')#Class initiated internally that derives an object.

var_1=2#object created for Integer Class.


#2.VALUE: it is a value of an object under Class.

#NOTE:Value of some objects can change, those are MUTABLE. value of some objects unchangeable, those are IMMUTABLE.

print(var_1)#it value returns

print(var_1.as_integer_ratio())#object has built-in attribute references as automatically displayed on console. these attributes supports on basis of type of object.

print(var_1.__ceil__())#object has special methods as automatically displayed on console. these attributes supports on basis of type of object

print(type(var_1.__ceil__()))#it returns type of object

#TYPE: it is a type of an object under Class.

#Type of object determines the operations that object supports and also defines possible values for that type of object.

print(type(var_1))#it returns the type of an object.

#NOTE:Object has TYPE and IDENTITY, they never changes once object has been created.

print(id(var_1))#it returns id(memory location) of an object.

#NOTE: we can check identities of objects using IS operator.

#IS operator: it compares identities of two objects

var_2=1.1314#object created under Float Class
print(var_2)#it prints objects value
print(type(var_2))#object type
print(id(var_2))#objects identity

#IDENTITY CHECKING: IS
print(id(var_1)is id(var_2))#it returns boolean value either TRUE or FALSE.

#Different Objects:
var_3=[1,2,3,4,5]
print(type(var_3))#LIST CLASS

print(var_3.append(6))#there are  built-in methods like append() after new type of object created. method appending item at end of the list.

var_4={1,2,3,4,5}
print(type(var_4))#SET CLASS

print(var_4.pop())#there are built-in methods like pop() after new type of object created. method pop remove and return item in the set.

var_5={'x':1,'y':2,'z':3,1:(1,2)}

print(var_5.keys())#these are built-in methods like keys() after new type of object created. method keys() returns Dictionary keys.

print(type(var_5))#DICT CLASS

#STRINGS:

#STRING is a sequence of values in range U+0000 - U+10FFFF, but python does not support CHAR type.
string_1='PYTHON'#String class initiated.
print(string_1)#returns object of string class.

print(ord('p'))#it built-in function which converts ccde form in the range U+0000 - U+10FFFF from string value.

print(chr(112))#it built-in function which converts integer to corresponding character.

print(string_1.encode())#converts string to bytes

string_2=b'PYTHON'
print(string_2)

print(type(string_2))#Bytes class

print(string_2.decode())#it converts bytes to string

print(string_1.capitalize())#these are built-in methods like capitalize()

print(type(string_1))#type of object
print(id(string_1))#id

# string_1[2]='d'#it is not supports.

#NOTE: print(string_1)#it raises error because string object is immutable.

#OBJECT REFERENCES:TYPE, VALUE

#MUTABLE TYPES:Type of an object affect on operations for Mutable types only.

print(2+3)#operations compute new value 5 may return reference to any existing object with same type and value.
print(type(2+3))#it returns must be Integer type.

print(2+1.1413)
print(type(2+1.1413))#it must be float type.

print(1.123-0.434)
print(type(1.123-0.4341))#it must be float type.

#EXAMPLE:MUTABLE TYPES

a=1;b=1# a and b may refer to same object with object value is 1
print(id(a));print(id(b))

x='hello';y='hello'#these may refer to same object with string value is hello

#IMMUTABLE TYPES:

a=[];b=[]# a and b are guaranteed to refer to 2 different, uniquely and newly created empty lists. it assigns same object to a and b.
print(id(a));print(id(b))

#IMMUTABLE TYPES:it does not affect on operations

print([1,2,3,4,5])#this object has only same type Integer

print([1,2,'a','python','$',1.23,12e34,1+1j,1-1j,-2j])#Different Types allowed.





























