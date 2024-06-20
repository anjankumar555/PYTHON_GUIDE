#IDENTATION: It is a leading whitespace at the begining of a logical line is used to determine the grouping of statements with respect to indentation level of line.

#Basically Indentation will appear in Fuction definition, Class definition, Exception handlers and Compound statements such as IF, FOR, WHILE etc...

#They are mainly used to execute a series or block of suitable statements execute at once based on condition

#Indentation is defined by colon symbol in python, if not given it raises error as TabError

#NOTE:Indentation is a TAB or 8 spaces throughout a line

#examples:In compound statements

#test a number even by IF

a=2#object defined
if a%2==0:#This is an Indentation, Tab or spaces
    print('even')#now indentation starts and automatically after 8 spaces allowing group of statements for execution
    pass#indentation over

#NOTE: FOR loop always for iteration 

a=[1,2,3,4,5,6,7,8,9]#defined a iterable object LIST. 
for x in a:#Indentation starts
    print(x)#group of statements
    pass#exit from identattoin
a=2
while a>3:
    print('loop starts')
    pass

#In fuction def:

def fun_def():#declaring function definition as per syntax
    print('Hello function def')#group of statement under indentation level
    pass#indentation completed for above function
fun_def()

def fun1_def(a):
    print('hello world')
    pass
fun1_def('Hello')

def fun1_def(a,x=1,y=2):
    print('third function')
    pass
fun1_def(1)

    

    
