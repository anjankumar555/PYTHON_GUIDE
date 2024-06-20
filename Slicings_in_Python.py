#SLICINGS:it selects a range of items in a sequence object. it is quiet different from Subscriptions which selects one item at a time.

#SLICNING:it 2 types:1.primary[expression] 2.proper slice

#SYNTAX:[Lower bound]:[Upper bound]:[Stride]

#Proper sice:Lower bound=Start;Upper bound=Stop;Stride=Step;

#a SEMICOLON used in between the lower,upper and stride. these are integers type.

#NOTE:Slicings may be used as Expressions or Targets in Assignment or DEL statements.

#SLICINGS:
primary_1=[1,2,3,4,5]#Sequence Object
print(primary_1)#prints the object

slic_1=primary_1[0:4]#Slicing the object

print(slic_1)#it slice from left to right(0 to 4)

slic_2=primary_1[-1:-5]#Slicing the object

print(slic_2)#it slice from right to left(-1 to -5)

#EXAMPLES:

slic_3=primary_1[0:-1]#this value equal to [0:4]
print(slic_3)

slic_4=primary_1[-1:0]
print(slic_4)#this value equal to [-1:-5]

slic_5=primary_1[-1:3];slic_6=primary_1[3:-1]

print(slic_5)#this value equla to slice_2 and slice_4

print(slic_6)

#SLICING with STRIDE/STEP value.

#NOTE: STEP/STRIDE value always positive integer.

#NOTE:Step is forwarded by its value.

slic_7=primary_1[0:3:1]#here 1 is a step value for slicing.
print(slic_7)

slic_8=primary_1[1:4:2]
print(slic_8)

slic_9=primary_1[0:4:3]
print(slic_9)

#DICTIONARY:
dic_1={'a':1,'b':2,'c':3,'d':4}
print(dic_1)

sub_1=dic_1['a']

print(sub_1)#this is subscription





