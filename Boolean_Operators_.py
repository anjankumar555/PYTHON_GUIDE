#To Demonstrate Boolean Operations.
#Boolean Operators:Boolean AND,Boolean OR,Boolean NOT.They write as and,or,not in the program.they do not have logical symbol.
#NOTE:these are different from Bitwise AND,OR,NOT.
print('BOOLEAN OPERATORS:')
print('''           and
           or
           not
           '''
      )
#NOTE:
#Boolean AND:x AND y means first evaluates x;if x is false,its value returned;otherwise y is evaluated and return result.
#NOTE:"False","None","0",'emptystrings' and "datacollections" are interpreted as false,other values are interpreted as true.
#AND returns last evaluated argument.
print('BOOLEAN AND:')
print(True and False)#False is false
print(False and True)
print(None and 1)#None is false.
print(1 and None)
print(None and None)
print(0 and None,None and 0)
print(1 and 2)#last evaluated argument as 2 is return.
print(0 and 1,1 and 0,0 and 0)#0 is false.
print(2 and 1)
print(0.00 and 0)
print(0 and 0.00)
print(-0 and 0,0 and -0,-0.00 and 0.00)
print(10 and 100)
print(1 and 2 and 3,1 and 2 and 3 and 4,1 and 2 and 3 and 4 and 5)
print(1.23 and 3.453)
print(1.34 and 1+4j and 3.45+3.4j and 1.14e3+3.4e4j)#arguments may be any type.
print(1.1434 and 1 and 2)
print(1e23 and 3e4)
print(14e-76 and 1.235 and 4 and 1.32e4)#it may be of any type.
print('p' and 'y')#including strings allowed for Boolean operations.
print('' and 'p','p' and '')#empty string always False
print('python' and 'java')
print('p' and 'y' and 't' and 'h' and 'o' and 'n')
print('python' and 'JAVA' and 'PYTHON' and 'angularJS')
print('python' and 'JAVA' and 'PYTHON' and 'angularJS' and 1.45 and 5e34  and '$')#arguments maybe anytype.
#NOTE:AND can also test for datacollections like LIST,TUPLE,SET,FROZENSET,DICT.
print(1 and 'I MISS YOU'and 'PYTHON'  in [1,2,3,'I MISS YOU',4,5,6,7,'PYTHON',8,9,0])#LIST object.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 in (1,2,3,4,5,6,7,8,9,0))#TUPLE object.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 in {1,2,3,4,5,6,7,8,9,0})#SET object.
print('P'and 'Y'and 'T'and 'H' in ['P','T','O','Y','H'])#String LIST object.
print(1 and 3 and 4 and 'i' and '$' in {0:23,1:'Python',2:3.454,3:'JAVA',4:13e433,'i':43,'$':'RAM'})
#NOTE:'OR' operation:x OR y means first evaluates x;if x is true,its value returned;otherwise y is evaluated and return result.
print('BOOLEAN OR:')
print(1 or 2)#it returns first evaluated argument if it is True.otherwise second is evaluated and return result.
print('Boolean operators on keywords:')
print(True or False)#False is false
print(False or True)
print(None or 1)#None is false.
print(1 or None)
print(0 or None,None or 0)
print(None or None)
print('Boolean operators on numerical literals:')
print(1 or o)#it not follows truth values of OR.
print(0 or 1)#in this case first argument is false so second is evaluated and returns 1.
print(0 or 0)#here first is false,second also false and returns.
print(0 or 0.00);print(-0 or 0.00);print(0.00 or -0.00);print(-0.00 or -0.00)
print(2 or 1)
print(1 or 2 or 3,1 or 2 or 3 or 4,1 or 2 or 3 or 4 or 5)
print(1.23 or 3.453)
print(1.34 or 1+4j or 3.45+3.4j or 1.14e3+3.4e4j)#it may be of any type.
print(1.1434 or 1 or 2)
print(1e23 or 34)
print(14e-76 or 1.235 or 4 or 1.32e4)
print('p' or 'y')#including strings allowed for Boolean operations.
print('' or 'p','p' or '')#empty string always False
print('python' or 'java')
print('p' or 'y' or 't' or 'h' or 'o' or 'n')
print('python' or 'JAVA' or 'PYTHON' or 'angularJS')#AND test for strings
print('python' or 'JAVA' or 'PYTHON' or 'angularJS' or 1.45 or 5e34  or '$')#arguments may be any type.
#NOTE:OR can also test for datacollections like LIST,TUPLE,SET,FROZENSET,DICT.
print('Datacollections under OR test:')
print(1 or 'I MISS YOU'or 'PYTHON'  in [1,2,3,'I MISS YOU',4,5,6,7,'PYTHON',8,9,0])#it not return boolean value.
print(1 or 2 or 6 or 7 or 9 or 3 or 5 in (1,2,3,4,5,6,7,8,9,0))#TUPLE object.
print(1 or 2 or 6 or 7 or 9 or 3 or 5 in {1,2,3,4,5,6,7,8,9,0})#SET object.
print('P'or 'Y' or 'T'or 'H' in ['P','T','O','Y','H'])#String LIST object.
print(1 or 3 or 4 or 'i' or '$' in {0:23,1:'Python',2:3.454,3:'JAVA',4:13e433,'i':43,'$':'RAM'})
#Boolean NOT:
#NOTE:NOT operator should be used after arguments.it returns always boolean value regardless of value and type of object.
#NOTE:NOT returns True if its argument is false,otherwise it returns False.
print('BOOLEAN NOT:')
print(not 4)#here argument 4 is True,so it returns False.
print(not 0)#here argument 0 is false,so it returns True.
print(not None)
print(not False)#any digit and character is interpreted as "true".
print(not True)
print(not 1)
print(not 'python')#even for strings.
print(not 'p')
print(not [1,2,3])#List
print(not (1,2,4))#for LIST,TUPLE,SET,DICT.
print(not 1.23e3+1.4e345j)
#Combination of AND,OR,NOT:
#NOTE:it should be first while use AND or OR.
print('AND,OR,NOT:')
print(not 'PYTHON' and 'java' or 'JAVA' or 'CPYTHON' or 3.45 and 5 and 12e4 or 1)
print(not 2 and 1 and 3)#evaluates from left to right.
print(not 2 and 1 or 3)
print('COMBINATIONS:AND,OR')
print(1 and 2 or 3 and 4)#last evaluated argument as 2 is return.
print(0 and 1 or 1 and 0 or 0 and 0)
print(2 and 1 or  43 or 33 and 321 and 100 and 200)
print(0.00 and 0 or 0 and 0 or 0 and 0)
print(0 and 0.00 or 0.00 or -0.00 and 0.000 and -0.000)#it is chain arbitrary.
print(-0 and 0,0 and -0,-0.00 and 0.00)
print(10 and 100 or 1000 or 10000)
print(10 and 100 or 1000 and 10000)
print(1 and 2 or 3 or 1 and 2 or 3 and 4 or 1 and 2 and 3 or 4 or 5)
print('p' and 'y'or 'a' and 'u' or 'o')#including strings allowed for Boolean operations.
print('' and 'p' or 'w' or 'p' and '')#empty string always False
print('python' and 'java' or 'JAVA' and 'PYTHON' or 'india' or 'hello')
print('p' and 'y' or 't' or 'h' and 'o' or 'n')
print(1 and 2 or 6 and 7 or 9 and 3 or 5 not in (1,2,3,4,5,6,7,8,9,0))
print(1 and 2 or 6 and 7 or 9 and 3 or 5  in (1,2,3,4,5,6,7,8,9,0))#NOT IN is a inverse result of IN.
print('P'and 'Y'and 'T'and 'H' in ['P','T','O','Y','H'])
print('P'and 'Y'and 'T'and 'H' not in ['P','T','O','Y','H'])#Negation of sequence.
#Combinations with BOOLEAN,COMPARISION operators:
print('BOOLEAN WITH COMPARISION operators:AND,IN')
print(1 and 3  in [1,2,3,4,5,6,7,8,9,0])
print(1 and 2 in [1,2,3,4,5,6,7,8,9,0])
print(13 and 14  in [1,2,3,4,5,6,7,8,9,0])
print(13 and 14 and 15 and 10 and 100 in [1,2,3,4,5,6,7,8,9,0])
print(1 and 3 and 14  in [1,2,3,4,5,6,7,8,9,0])
print(1 and 2 and 3 in [1,2,3,4,5,6,7,8,9,0])#using 'AND' logic,returns True.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 in [1,2,3,4,5,6,7,8,9,0])
print(1 and 'I MISS YOU'and 'PYTHON'  in [1,2,3,'I MISS YOU',4,5,6,7,'PYTHON',8,9,0])#LIST object.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 in (1,2,3,4,5,6,7,8,9,0))#TUPLE object.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 in {1,2,3,4,5,6,7,8,9,0})#SET object.
print('P'and 'Y'and 'T'and 'H' in ['P','T','O','Y','H'])#String LIST object.
#Combinations with BOOLEAN,COMPARISION operators:OR,IN
print('BOOLEAN WITH COMPARISION operators:OR,IN')
print(1 or 3  in [1,2,3,4,5,6,7,8,9,0])
print(1 or 2 in [1,2,3,4,5,6,7,8,9,0])
print(13 or 14  in [1,2,3,4,5,6,7,8,9,0])
print(13 or 14 or 15 or 10 or 100 in [1,2,3,4,5,6,7,8,9,0])
print(1 or 'I MISS YOU'or 'PYTHON'  in [1,2,3,'I MISS YOU',4,5,6,7,'PYTHON',8,9,0])#LIST object.
print(1 or 2 or 6 or 7 or 9 or 3 or 5 in (1,2,3,4,5,6,7,8,9,0))#TUPLE object.
print(1 or 2 or 6 or 7 or 9 or 3 or 5 in {1,2,3,4,5,6,7,8,9,0})#SET object.
print('P'or 'Y'or 'T'or 'H' in ['P','T','O','Y','H'])#String LIST object.
#NOTE:Neither AND nor OR restrict the value and type they return to False and True.


