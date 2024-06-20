#to demonstrate FOR control statement
#FOR statement is used to iterate over the elements of iterable objects like LIST,SET,TUPLE,STRING etc..
#Syntax:(for (variablename) in (iterable object)):
print('FOR statement Syntax:')
for a_1 in 1,2,3,4,5,6:#iteration over elements.
    print(a_1)#finally printed after iteration one by one on console.
for a_2 in 0,1,2,3,'a','p','HELLO',5:#iterable objects
    print(a_2)
else:
    print('Loop Fails')
#FOR loop in DataCollections:
for x in (1,2,3,4,5):#'x' is an identifier or any variable.
    print(x)
else:
    print('loop unsuccess')
for v in [1,2,3,4,5]:#it must be iterable objects only.
    print(v)
else:
    print('loop unsuccess')
for i in range(10):#FOR in built-in functions
    print(i)
else:
    print('loop unsuccess')
#NESTED FOR loops:
print('Nested FOR loop:')
for x in [1,2]:
    for y in [3,4]:
        for z in [5,6]:
            print('Hello')
else:
    print('Loop fails')
#Nested Loops:

#Two variables in Loop at a time:
print('FOR loop with 2 variables:')
for x,y in [0,1],[-1,-2]:#if we use 2 variables items must be 2 in the ierable objects
    print(x,y)
for x,y,z,t in (1,2,3,5),[0,-2,5,7],[0,1,5,6] ,[-1,-2,4,3]:#4 variables and 4 values or items.
    print(x,y,z,t)
#NOTE:ELSE clause is always optional in all loops OR control flow statements.
print((1 if 1<4 else -1),(3 if 2<3 else 0),(5 if 1<4 else -1)*[3 if 2<3 else 0])#Starred Expression.
print((4 if 0<1 else 'unsuccess')*[6 if 5>4 else -1])#this means 4 times 6 is printed as a LIST.i.e..4*[6]
print((8 if 0<1 else 'FALSE')*[1,2,3,4,5])#Expression List.it means 8*[1,2,3,4,5]
#Syntax FOR loop: for Variable/Identifier in Expression List:suite of statements;else:suite of statements.
print('another way to FOR loop:')
for x in [0,-1,-2,-3] if 0<1 else -1*[1,2,3,4,5]:
    print('Loop Success')
for x in [0,-1,-2,-3] if 0>1 else -1*[1,2,3,4,5]:
    print('Loop Success')
#Combinations of Loops:
print('combinations of FOR,WHILE and IF')
for x in [1,2,3,4,5]:#iterable object.
    if len([1,2,3,4,5])==5:#Builtin function in FOR loop.TRUE
        while len([1,2,3,4,5])>5:#it FALSE.so loop terminates and ELSE block executed.
            print('loop success')
else:
    print('loop fails')
#combinations:
for x in [1,2,'python','H',4,5]:
    if any([1,2,'python','H',4,5])==True:#builtin function
        while (all([1,2,'python','H',4,5]))==False:#builtin function
            print('loop success')
else:
    print('loop fails')
#combination:
for z in (1,2,3,5,0):
    while z==1000:
        if z>-1:
            print('Loop success')
            

