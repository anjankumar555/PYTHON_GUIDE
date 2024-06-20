#Pass Statement: Pass statement is a null operation but no code needs to be executed

#Pass statement executed nothing is happens, so a statement is required syntactically

#NOTE: Pass basically used in control flow statements, callable types and any code of block(Indentation)

#control flow statements:

#Examples:

v_1=3
if v_1%2!=0:#checking condition for indentation
    print('odd number')
    pass#this is out passed the block of code or loop


x=2020
if x%2==0:
    print('x is even number')#block of statements
    pass#ends block of code 
else:
    print('x is odd number')
    pass#ends else clause

#NOTE: Above code pass statement does nothing in code of block but it used to exit from the code of block body and it is always optional 

y=[1,2,3,4,5,6,7,7,8,9,0]
for i in y:#iterable items in list 
    if i%2==0:#checking condition for each item
        print('even number')
        pass#it ends inner block of code or loop IF1
    if i%2!=0:
        print('odd number')
        pass#it ends inner block 2 of code or loop IF2
    pass#it ends outer block of code or loop FOR

z=0
while z>0:#False 
    print('hello world')#block suite of statements
    pass#block of ends

#Callable Types:

def f(a):pass#function and body terminates at a time

class a():pass


def f():#defining function object
    pass#body of function ends
f()

class c:#defining class objects
    pass#ends class body 
b=c







