#To demonstrate the Datacollections are LIST,SET,TUPLE,DICTIONARY and FROZENSET.
#To construct  datacollections,Display syntax used.
#Display 2 types:1.starred 2.comprehension

#LIST is empty series of expressions enclosed in square brackets.
#Elements may be any datatypes:int,float,char and string.
#NOTE:LIST is MUTABLE(different datatype contents)
#MUTABLE:it means it support item assignment.

#MUTABLE OBJECTS:LIST, DICTIONARY.it means unhashable.mutable objects can change their value but their identity remains same.
#IMMUTABLE:TUPLE, SET and FROZENSET.
#IMMUTABLE: it means Hashable, an object is hashable if it has a hash value which never changes during lifetime. hashable objects must have same hash value.

#LIST display:[starred list]
print('Starred LIST:')
print((1 if 1<4 else -1),(3 if 2<3 else 0)*[1,2,4,5,6,8,7,9])#Starred LIST.it displays LIST on console.
print((2**3)*[1,2,3])

#Note: List Unpacking by using single asterisk(*) and also for SET, TUPLE
print(*[3],*[1,2,4],*[5,6])#Unpacking items in List.
print(*range(9))#Tuple unpacking
print({*range(9)})#SET Unpacking


#LIST:
print('Data type:LIST')
print([0,1,2,3,4,5,6,7,8,9])
print([0,-2,-1,3,4,1.2,4.9,-0.8,-3.4,1e23,1.23e3,1+2j,-1+3j,1e34+4.34j])
print([0,2,-3,6.7,-1.24,1.34e2,1+3j,2.34e3+1e4j,'python','H'])#it contains all data types as items.
List=[1,2,3,4,5,6];List[0]=0#List is mutable, so that we can assign item.
print(List)#after assignment List is [0,1,2,3,4,5,6], here 1 is eliminated.

#NESTED LIST:list within list.
print([1,2,[1,2],4,[5,6]])
print([[1,2],[3,4],5,6,7,[8,9,0]])
print([[[[[0]]]]])#Nested List.-pio8


#NOTE:SET is IMMUTABLE:it means SET does not support item assignment.

print('Data type:TUPLE')
print((0,1,2,3,4,5,6,7,8,9))#TUPLE
print((0,-2,-1,3,4,1.2,4.9,-0.8,-3.4,1e23,1.23e3,1+2j,-1+3j,1e34+4.34j))#TUPLE:only numerical datatype
print(type((0,-2,-1,3,4,1.2,4.9,-0.8,-3.4,1e23,1.23e3,1+2j,-1+3j,1e34+4.34j)))


#SET:these are series of elements enclosed in braces.
#SET is IMMUTABLE.

print({0,1,2,3,4,5,6,7,8,9})#SET
print({0,-2,-1,3,4,1.2,4.9,-0.8,-3.4,1e23,1.23e3,1+2j,-1+3j,1e34+4.34j})#SET
print({0,2,-3,6.7,-1.24,1.34e2,1+3j,2.34e3+1e4j,'python','H'})#it contains all data types as items.
print({1,2,3,{4,5},7,0,{9}}#Nested Set

#TUPLE:
#IMMUTABLE sequences and used to store heterogenous data

#NOTE:one or more elements seperated by comma is TUPLE.

#NOTE:parenthesis is always optinal in TUPLE,it implements all sequence operations.

#NOTE:built-in function tuple,we can form TUPLE from other data collections.
print('TUPLE data collections:')      
print(1,)#Singleton TUPLE
print((1,))#it is also a TUPLE,seperated by comma.
print(1,2,3)#tuple
print(type((1,2,3)))
print((1))#not a TUPLE
print(type((1)))#Integer type data not TUPLE
print(type(()))#EMPTY TUPLE
print((1,2,3,4,5,6,7,8,9))
print((1,0,-1,'a','P','python',-1+3j,12.3e4))
print(tuple([1,2,3]))#LIST becomes TUPLE 
print(tuple('PYTHON'))#using builtin function.
print(tuple({1,2,3}))#form TUPLE.

#DICTIONARY:it contains Key-Value pairs.it is enclosed in braces.Dictionary is series of Key and value pairs.
#Dictionary later values always override earlier ones.
#Dictionary is mutable.

print({0:-1,1:-2,2:-3,3:-4.3})#0 is Key and -1 is value,-2 is value for corresponding Key 1 and so on.
print(type({0:-1,1:-2,2:-3,3:-4.3}))#DICT
print({0:1.33e2,3:1+4j,'a':'PYTHON',-1:'Hello',4:'f'})#Different Keys contain Differeent Values

#DICTIONARY:it contains Key-Value pairs.it is enclosed in braces.

print({0:-1,1:-2,2:-3,3:-4.3})#0 is Key and -1 is value,-2 is value for corresponding Key 1 and so on.
print(type({0:-1,1:-2,2:-3,3:-4.3}))#DICT
print({0:1.33e2,3:1+4j,'a':'PYTHON',-1:'Hello',4:'f'})#Different Keys contain Differeent Values

#get() method is used to access value in dictionary.
#Note:If Dictionary has same key for all values, then it returns final dictionary value for that key.

#Note: Dictionary not support arthmetic operations such as Addition, Subtraction, Multiplication and Division.
#Note: Dictionary unpacking using double asterisk(**)
print('Dictionary:')
Dict_1={'a':1,'b':2,'c':1e34,'d':'PYTHON'}#Dictionary
Dict_2={'a':1,'a':2,'a':1e34,'a':'PYTHON'}#Dict_2 has same key for all values.
print(Dict_1)#printing Dict_1
print(Dict_2)#printing Dict_2 of last value which have given.
print(Dict_1.get('a'))#accessing value from key.
print(Dict_1.get('d'))#it return value
print(Dict_2.get('a'))#it returns always final value.

#Dictionary Unpacking:
print(dict(**{'x': 1}, y=2, **{'z': 3}))#it returns Unpacking using ** for dictionary.

#Note:GENERATOR EXPRESSIONS demonstration: it should know before COMPREHENSION in Python.

#GENERATOR EXPRESSIONS:it is a compact generator notation in parentheses. it is an expression that returns iterator.
#it is normal expression followed by a FOR clause loop variable, range  and IF clause (optional always)
#Generator Expressions syntax is same as comprehensions except enclosed in curly brackets.
#SYNTAX:(Expression Comprehension for)
#it returns a new generator object
print((x**2 for x in [1,2,3,4,5]))#first expression and then for clauses in iterable.
print((y+2 for y in {1,2,3,4,5}))#first expression and then for clauses in iterable.
print(a*b for a in [1,2,3] for b in [4,5,6])#it returns object of gen expression.
print(c*d for c in range(4) for d in range(6))
print(c*d for c in range(2) for d in range(c,c+4))
print((x**2 for x in [1,2,3,4,5] if x>5))
print(sum(i*i for i in range(10)))#it is GENERATOR EXPRESSION.


#2.COMPREHENSION:it computed via set of looping and filtering.

#NOTE:it consists of single expression followed by atleast one FOR clause and zero or more FOR or IF clauses.

print('Comprehension examples:')
print('LIST Comprehension:')
print([x+2 for x in [1,2,3,4,5]])#LIST Comprehension for addition.
print([x**2 for x in [1,2,3,4,5]])#LIST Comprehension for power.
print([x/2 for x in [2,4,6,8,20,40]])#LIST DISPLAY second form.

#NOTE:FOR loop in LIST COMPREHENSION,it returns as per number of iteration over the items present in the iterable objects LIST,SET,DICT,TUPLE.

print([x*2 for x in [1,2,3,4,5] for y in [6,7,8,9,10]])#more than one FOR loop.it returns each item 5 times in LIST as output.
print([x*2 for x in [1,2,3,4,5] for y in [6,7,8,9,10] for z in [-1,2,-3,4,-5]])#it returns each item 25 times after evaluation of expression in LIST as output.
print([x//2 for x in [2,4,6]])#it returns LIST [1,2,3].
print([x//2 for x in [2,4,6]for x_1 in [1,3,5]])#it returns each item 3 times as above LIST.
print([x//2 for x in [2,4,6]for x_1 in [1,3,5]for x_2 in [1,2,3]])#it returns 9 times as above LIST.
print([x//2 for x in [2,4,6]for x_1 in [1,3,5]for x_2 in [1,2,3]for x_3 in [0,5,8]])#it returns 27 times as above LIST.
print([x//2 for x in [2,4,6]for x_1 in [1,3,5]for x_2 in [1,2,3]for x_3 in [4,5,6]for x_4 in [8,3,7]])#it returns 81 times as above LIST.


#LIST comprehension:
print([2+3*2 for x in [1,2,3]if x>2])#single expression with atleast one FOR and more than one IF clause.
print([x**2 for x in [1,2,3]if x%2!=0 if x==1])#2 IF clauses used.
print([x_1//2 for x_1 in [2,4,6,8,10,40]for x_2 in [1,2,3]if x_1>10 if x_2%2==0 if x_1>30])#atleast FOR and more FOR or IF clauses is possible.
print(['EVEN'if x%2==0 else 'ODD'for x in [0,1,2,3,4,5,6,7,8,9]])#finding Even and Odd number from 0 to 9.


#NOTE:List comprehensions evaluating expression  from left to right to produce item each time innermost block is reached.
#NOTE:later any IF clauses present,filter the items finally. 

print(['odd' for x in range(10)if x%2!=0])#comprehension in builtin functon.
print([x*2 for x in range(5)])#using range()built-in function.
print([x+2 for x in range(0,5)])
print([x_1/2 for x_1 in range(1,10)if x_1>8])#if clause 
print([x*y for x in range(3)for y in range(5)])#using more FOR clauses
print([x*y for x in range(3,5)for y in range(5,7)if x>3 if x>5 if x<7 if x!=0])#Using more FOR clauses and IF clauses
print([x*y for x in range(3)for y in range(x,5)])#using inner most loop
print([(x*y+z) for x in range(3)for y in range(x,x+5)for z in range(5)])#Expression is evaluated first and passed argument to nestedscope implicitly.

#LIST Supported operations:
#Arthmetic operations:it supported Addition only.
print('LIST supported operations:')
print([1,2,3]+[4,5,6])#combined 2 LISTS
print([1,2,3]+[4,5,6]+[7,8,9])#combined 3 lists
print(3*[4,5,6])#3 times printed LIST.

##SET is empty series of expressions enclosed in  curly braces.
#Elements may be any datatypes:int,float,char and string.
#NOTE:SET is MUTABLE(different datatype of contents)
#MUTABLE:it means changable
print('SET display"')
print({0,1,2,3,4,5,6,7,8,9})#SET

#SET supported operations:
#Arthmetic operations:it supported subtraction only.
print('SET supported operations:')
print({4,5,6}-{1,2,3})#it returns first set.
print({4,5,6}-{4,5,6})#it returns set()

#EMPTY SET:it means DICTIONARY in Python.
print({})#not contains any items in set.
print({0})#it not a empty set,it is zero set.
print(type({}))#not a empty set.

print('SET from Expressions:')
print({1+3/2*1,2//2,3**2,4*1-2})#expressions
print({1,2,-2,1e34,1.23,3.12e3,-1+2j,1e3+3.4e54})#numerical SET
print({1,'a','P','String',2,1e34})#different dataset

#COMPREHENSION: 
print('SET COMPREHENSION:')
print({x+2 for x in [1,2,3,4,5]})
print({x**2 for x in [1,2,3,4,5]})
print({x*2 for x in [1,2,3]if x%2!=0 if x==1})#2 IF clauses used.
print({x_1//2 for x_1 in [2,4,6,8,10,40]for x_2 in [1,2,3]if x_1>10 if x_2%2==0 if x_1>30})#atleast FOR and more FOR or IF clauses is possible.
print({'EVEN'if x%2==0 else 'ODD'for x in [0,1,2,3,4,5,6,7,8,9]})#finding Even and Odd number from 0 to 9.

print({'odd' for x in range(10)if x%2!=0})#comprehension in builtin functon.
print({x*2 for x in range(5)})#using range()built-in function.
print({x+2 for x in range(0,5)})
print({x*y for x in range(3)for y in range(x,5)})#using inner most loop
print({(x*y+z) for x in range(3)for y in range(x,x+5)for z in range(5)})#Expression is evaluated first and passed argument to nestedscope implicitly.

#COMPREHENSION:Tuple
print('TUPLE COMPREHENSION:')
print((x+2 for x in (0,1,2,3,4,5))#it returns objects of Tuple, not in the form of Tuple.
print((x*2 for x in (0,1,2,3,4,5))#objects Tuple
print((x/2 for x in (2,4,6,(12,44,46),88))#Tuple Objects.

#COMPREHENSION:Dictionary
print('Dictionary:')
print({'a':1,'b':2,'c':1e34,'d':'PYTHON'})
print({x:x+2 for x in [1,2,3]})#Comprehension Dictionary
print({x: x**2 for x in [1,2,3,4,5]})#Dictionary Comprehension.
print({x:x/2 for x in range(2,20)})

#FROZENSET:it is to represent sets of sets, i.e.,inner sets.it has characteristics of a SET.
#FrozenSet can be created using Built-in function frozenset().
#SYNTAX:frozenset(ITERABLE OBJECT).
#Frozenset is IMMUTABLE(Hashable)
print({1,2,3,4,5,6,7})#this is a set.
print({1,2,3,4,5,6,7})#this is a set.
print(frozenset({1,2,3}))#Iterable set object inside function
print(frozenset([1,2,3]))#Iterable LIST object inside function
print(frozenset((1,2,3)))#Iterable TUPLE object inside function
print(type(frozenset((1,2,3))))#Iterable set object inside function
















    
