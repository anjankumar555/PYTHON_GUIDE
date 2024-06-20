#ARGUMENT: A Value passed to a function or a method when calling the function.here we disscuss about arguments.

#Basically two kinds of arguments in python.

#1.Keyword 2.Positional 

#1.Keyword: an argument preceeded by an identifier in a function call or passed as value in a dictionary preceeded by **

#Syntax:primary_1(value_1=2,value_2=3)here value_1, value_2 are identifiers.

#it passes value in a dictionary preceeding by double asterisk ** symbol
dict(**{'A':2,'B':4,'C':6})#this is a dictionaty containing keyword arguments. they must be strings.
print(dict(**{'A':2,'B':4,'C':6}))#it returns dictionaty.2,4,6 are keyword arguments in dictionary.

complex(**{'real': 3, 'imag': 5})#it passes values in a complex method or callable object.
print(type(complex))#it returns type of complex.
print(complex(**{'real': 3, 'imag': 5}))#it returns a complex number

#Positional: An argument can appear at the bigining of an argument list or passed as elements of iterable precceded by *
#iteable:sequence object such as list, Set, Tuple...

#NOTE:Postional arguments follows keyword arguments always.
#Syntax:primary_1(value1,value2,value3,value4....)

complex(1,1)#These are positional arguments passed as values in complex buit-in method.
print(complex(1,1))#it prints a complex number, here 1,1 are positional arguments.

sum([0,1,2,3,4,5,6,7,8,9])#These are positional arguments as iterable as a LIST.
print(sum([0,1,2,3,4,5,6,7,8,9]))
#NOTE:positional arguments can be iterable objects such as LIST, SET, TUPLE...

pow(2,3)#these are positional arguments.
print(pow(2,3))

print(sum((0,1,2,3,4,5,6,7,8,9)))#Positional arguments as TUPLE.

print(sum({0,1,2,3,4,5,6,7,8,9}))#Positional arguments as SET.

range(10)#it is an argument passed as value in a builtin function.
print(range(10))#it returns values from o to 9 as default positional arguments.

#NOTE:An expression can represent an argument.

#these are arguments discussed without function definition and body.