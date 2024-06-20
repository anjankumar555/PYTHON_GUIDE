#To Demonstrate Primaries in Python
#Primaries:these are most tightly bound operations/Expressions in language.
#Primaries are 5 types in python:ATOM,ATTRIBUTEREF,SUBSCRIPTION,SLICING and CALL.
#Atom:it is simply like an identifier/literal and also enclosed in brackets,braces,paranthesis etc..
#Atom:syntax
x=0#'x' is an identifier and 0 is a value binding to any name or character.
primary=1_0;primary_1=2_0;primary=5_6_7#identifiers may be names or any characters and 10,20 values binding to names primary,primary_1.
#NOTE:name refer to an object.value is binding to name or identifier.
#10=x,20=y is wrong binding
#NOTE:Atoms may be identifier or Literal or any parenthesis form.
print([3+4/5])#Starred Expression
print([3+4/5])#Parenthesized form
print(type(([3+4/5])))#LIST
print([3+4/5,5-3*2/2,4//2])
print(type([3+4/5,5-3*2/2,4//2]))#LIST
print([3+4/5,5-3*2/2,4//2],[4%2+1,2+7/3])
print(type((3+4/5,5-3*2/2,4//2)))#TUPLE
print((1 if 1<4 else -1)*[1,2,4,5,6,8,7,9],(3 if 2<3 else 0)*[1,2,4,5,6,8,7,9])#Expression LIST.
print((1 if 1<4 else -1),(3 if 2<3 else 0)*[1,2,4,5,6,8,7,9])#Starred LIST.
print((1 if 1<4 else -1),(3 if 2<3 else 0),(5 if 1<4 else -1)*[3 if 2<3 else 0])#Starred Expression.
#LIST display:LIST display is empty series of expressions enclosed in square brackets.it is 2 types:1.STARRED LIST,2.LIST COMPREHENSION.
#in Starred LIST * is used for unpacking.it returns LIST.
print((1 if 1<4 else -1),(3 if 2<3 else 0)*[1,2,4,5,6,8,7,9])#Starred LIST.

