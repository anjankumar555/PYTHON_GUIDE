#To demonstrate Membership Testing using Operators
#The following Operators test the member of group,sequence or mapping objects.
print('MEMBERSHIP TEST OPERATORS:')
print('''  'IN'  'NOT IN'  ''')
print('Membership test in sequences or datacollections:')
print(3 in [1,2,3,4,5,6,7,8,9,0])#it returns True if 3 is member of sequence or list object,False otherwise.
print(30 in [1,2,3,4,5,6,7,8,9,0])#it returns True if 30 is member of sequence or list object,False otherwise.
#NOTE:'NOT IN' is the inverse truth value of 'IN' operator.
#NOTE:'IS NOT' is the inverse truth value of 'IS' operator.
print(3 not in [1,2,3,4,5,6,7,8,9,0])#Inverse membership operator.
print(13 not in [1,2,3,4,5,6,7,8,9,0])#it returns True if 13 is member of sequence or list object,False otherwise.
print([1,2] in [1,2,3,4,5,6,7,8,9,0])#here [1,2] is a another list object which not found.
print([1,2,3,0] in [1,2,3,4,5,6,7,8,9,0])#here [1,2,3,0] is a another list object which not found.
#NOTE:Only one element can be test without parenthesis,square and flower brackets.
#NOTE:we can check using 'AND' operator explicitly for more than one item.
print(1 and 3  in [1,2,3,4,5,6,7,8,9,0])#using 'AND' logic,returns True
print(1 and 2 in [1,2,3,4,5,6,7,8,9,0])#using 'AND' logic,returns True.
print(13 and 14  in [1,2,3,4,5,6,7,8,9,0])#using 'AND' logic,returns True.
print(13 and 14 and 15 and 10 and 100 in [1,2,3,4,5,6,7,8,9,0])#using 'AND' logic,returns True.
print(1 and 3 and 14  in [1,2,3,4,5,6,7,8,9,0])#using 'AND' logic,returns True.
print(1 and 2 and 3 in [1,2,3,4,5,6,7,8,9,0])#using 'AND' logic,returns True.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 in [1,2,3,4,5,6,7,8,9,0])#using 'AND' logic,returns True.
#NOTE:if all elements in sequence are members except one or more,it returns False as per 'AND' logic.
print(1 and 2 and 6 and 7 and 9 and 3 and 15 in [1,2,3,4,5,6,7,8,9,0])
print(1 and 2 and 6 and 7 and 9 and 13 and 15 in [1,2,3,4,5,6,7,8,9,0])
print(1 and 2 and 6 and 7 and 19 and 13 and 15 in [1,2,3,4,5,6,7,8,9,0])
#DataCollections of objects in membership test.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 not  in [1,2,3,4,5,6,7,8,9,0])#LIST object.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 in (1,2,3,4,5,6,7,8,9,0))#TUPLE object.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 in {1,2,3,4,5,6,7,8,9,0})#SET object.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 not in {1,2,3,4,5,6,7,8,9,0})#SET object.
print(1 and 2 and 6 and 7 and 9 and 3 and 5 not in (1,2,3,4,5,6,7,8,9,0))#Inverse membership operator.
print(1 and 2 and 6 and 7 and 'INDIA' and 'L' and 'a'  in [1,2,3,4,5,6,7,8,9,0,'A','INDIA','a','L'])#LIST object.
print(1 and 'I MISS YOU'and 'PYTHON'  in [1,2,3,'I MISS YOU',4,5,6,7,'PYTHON',8,9,0])#LIST object.
print('P'and 'Y'and 'T'and 'H' in ['P','T','O','Y','H'])#String LIST object.
print('P'and 'Y'and 'T'and 'H' not in ['P','T','O','Y','H'])#Negation of sequence.
print('P'and 'Y'and 'T'and 'H' in ('P','T','O','Y','H','python'))
print('python' in ['P','T','O','Y','H','python'])
#String and Bytes Literals:
print('Membership testing in Strings and Bytes Literals:')
print('H' in 'PYTHON')#Sub-string 'H' member of PYTHON.
print('H'and 'P' in 'PYTHON')
print('H'and 'p'and 'Y' and 'T' in 'PYTHON')
print(b'H' in b'PYTHON')#BYTES objet.
print('h' in 'PYTHON')#all uppercases except 'h'.
print('H' and 'j' in ('PYTHON','java'))
#NOTE:Empty strings always considered a sub-string of any other strings.
print('' in 'PYTHON ')#empty string.
print('' and ''and 'java' in ('PYTHON','java','C','C++','c#'))
print('' and ''and '#'and '+' in ('PYTHON','java','C','C++','c#'))
