#FUNCTIONS: A series of statements which returns some value to caller. it can also be passed zero or more arguments which may be used in the execution of body.

#NOTE: Function arguments are always optional but they are used for execution of function body which contains a series of statements. These are highly essential parts of code.

#Syntax: Decorators def function name(parameters or arguments)->expression:(Indentation)Suite

#In above syntax Decorators,Parameters and expression are optional.

#Suite is a series of statements and function name may be anything.

#Functions Definition:'def' is a keyword for declaring function definition

#Fuctions in python is also objects under Class declaration


#Example1:

def fun_1():pass #this is function declaration

def account_info_():return #this is function declaration

#Note: Try to use more single and small functions for single purpose in programs and give them to meaningful names.

def fun():#This is Function defintion along with name without parameters or arguments
    #Indentation in fuction boby or series of statements starts
    pass#This is optional statement in function 
#Out of Indentation

fun()#Calling function then execute a block of code or series of statements.

print(type(fun))#it is also an object under Fuction class

#Embed all operations with single fuction.

#Example:Data-Related operations

def process_data():# code of statements to READ, CLEAN and Generate the Data.
    pass
#Additional smaller functions:

def read_data_from_path(filepath):#it is READ data by providing path as an argument string
    return data

def clean_data(data):#smaller fuction
    return cleaned_data

def generate_report(cleaned_data):#smaller fuction
    return report

# Note: A name of the function is fun in above, but it is basically a variable or identifier implicitly inside python. so that it reflects operations based on the type of variable as per standard hierarchy.

#NOTE:when we declare function definition we must call them at end, orelse it never executes

#By calling function name finally for execution of statements or else never executes.

def fun1_1(a):#A single positional parameter
    print('Hello function')
    pass#end of function or indentation
fun1_1('Hello')#we can also pass argument as a string. because it is also a value in python

def fun1_2(a='Hello world'):#A single keyword parameter
    print(a)#function body
    pass
fun1_2()#calling function with out arguments because already declared in function def

def fun1_3(a=None):#This parameter has None value, it means no value
    print('Hello None function type')
    pass
fun1_3()#so that it values not declared at end

#Function Annotations:Annotations specifies the expected type for a variable or a function parameter or return value

#it is a label associated with variable or fuction parameter

#these also called type hint but these are optional

#Examples:

def fun(a:int,b:float)->float:#Fuction Annotations
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
    return a,b
fun(20,10.50)#thses values convert into float type

def fun_11(name:str)->str:
    print(name)
    pass
fun_11(5)#this value convert into string

#Example2:Function types

def fun_1():#no parameters
    print('Function block1 executes successfully')
    pass
fun_1()#it executes body of function and prints statement

#Example3:

def fun_2(a,b):#positional parameters in function def 
    print(a+b)#suitable code and addition of operation
    pass
fun_2(10,20)#calling function along with arguments for execution of function body

#NOTE:If we not pass arguments in calling function, it raised Error as missing argument

#Example4:

def fun_3(x,y=20):#Positional or keyword parameters
    print(x*y)#multiplication #we can declare values and must pass arguments in function calling
    pass
fun_3(10)#we declare positional argument only and already declared keyword parameter
#fun_3() this is calling a function without arguments, it raises Error
#Example5:

def fun_4(A,B,/,C=30,D=100):#Positional only parameters in fun def
    print(((A+B)*C/D))#operation of arguments
    pass#out of function body
fun_4(10,20)#calling arguments in function calling

#Example6:

def fun_5(a,b,c,*,x=5,y=6,z=7):#Keyword Only parameters in fun def
    print((a+b+c/x+y+z))#body of function or statements
    pass
fun_5(10,20,30)#calling arguments of positional and no need of keyword which already declared in function def

#Example7:

#NOTE: An arbitrary sequence of positional or keyword arguments we can pass in fun def

def fun_6(*pos_args,**key_args):#we can define any number of positinal or keyword as a sequence
    print(pos_args,key_args)
    pass
fun_6(0,1,[2,3,4,5],x=6,y=7,z=8,z_1=9,z_2=11,z_3=12)#here just call their arguments while declaratoin

def fun_7(a,b,c,*args,x=34,y=67,z=87,**keyargs):#An arbitrary sequence of positional or keyword arguments we can pass in fun def in addition to other parameters 
    print(a,b,c,args,x,y,z,keyargs)#print arguments
    pass
fun_7(1,2,3,[0,4,5,6,7],[8,9,10],[11,1,2,23,55,76],x1=34,x2=45,x3=678)#we can passing arguments also apart including other positional parameters a,b,c and keyword parameters x,y,z

#Function practical example:

def fun1(a,b):
    print(a+b)#addition
    pass#this is end of function1
def fun2(a,b):
    print(a-b)#subtraction
    pass#this is end of function2
def fun3(a,b):
    print(a*b)#multiplication
    pass#this is end of function3
def fun4(a,b):
    print(a/b)#division
    pass#this is end of function4
def fun5(a,b):
    print(a%b)#modulus
    pass#this is end of function5
fun1(20,10)#For every call needs for every function
fun2(20,10)#every time we need to call function for arguments of parameters
fun3(20,10)#every time calling then only execute function of body
fun4(20,10)
fun5(20,10)

#To overcome above problem we go for Nested Functions:

#Nested Function: A function can defined within scope of another function.

def outer_fun():#puter function without parameters
    print('Outer function')#body of outer function
    def inner_fun():#inner function without parameters
        print('Inner funciton')#body of inner function
        pass#end of the inner function or indentation  inner block
    inner_fun()#First calling inner fuction
    pass#end of outer function or indentation outer block
outer_fun()#Now calling outer function after inner function

#NOTE:Nested function executes all statements together within the scope of other function by parent function

#Example:In above example modified by Nested Fuctions

def fun1_1(a,b):#This is a outer or parent function
    print(a+b)#body of outer function for addition only
    def fun1_2(a,b):#this is inner1_2 of parant function
        print(a-b)#body of inner1_2 or parent
        def fun1_3(a,b):#this is inner1_3 of parent function
            print(a*b)#body of inner1-3 or parent
            def fun1_4(a,b):#inner1_4
                print(a/b)#body
                def fun1_5(a,b):#inner1_5
                    print(a%b)#body
                    pass#end of inner1_5 block only
                fun1_5(20,10)#calling fun1_5 function first to execute fun1_5 def
                pass#end of inner1_5
            fun1_4(20,10)#calling fun1_5 function first to execute fun1_5 def
            pass#end of inner1_4
        fun1_3(20,10)#calling fun1_5 function first to execute fun1_5 def
        pass#end of inner1_3
    fun1_2(20,10)#calling fun1_5 function first to execute fun1_5 def
    pass#end of inner1_2
fun1_1(20,10)#Now calling parent or outermost function fun1_1

#Example:

#Nested functions with conditions:

def fun1_1(*args,x=10,y=11,z=12):
    if args and x or y or z>0:
        print(args,x,y,z)
        pass
    else:
        print('No arguments to print')
        pass
    def fun1_2(a,b,c):
        if a and b and c>1:
            print(a,b,c)
            pass
        else:
            print('No arguments to print')
            pass
        def fun1_3(a=None):
            if a is None:
                print('Hello world')
                pass
            elif a>0:
                print('Positive')
                pass
            def fun1_4(a):
                if a>0:
                    print('positive')
                    pass
                elif a<0:
                    print('negative')
                    pass
                else:
                    print('non count number')
                    pass
                def fun1_5(a,b,c,d):
                    if a%2==0:
                        print('even')
                        pass
                    else:
                        print('odd')
                        pass
                    pass
                fun1_5(1,2,3,4)
                pass
            fun1_4(45)
            pass
        fun1_3()
        pass
    fun1_2(2,3,4)
    pass
fun1_1(1,2,3,[4,5,6,7],[8,9,0])

#Example:

def outer_f():#this is outer function or parent 
    x=1#declared variable in parent fuction
    def inner_f(a):#inner fuction of parent fuction
        print(a+x)#it access value x from outer function
        pass#out of inner function
    inner_f(2)#calling inner
    pass#out of outer function
outer_f()#calling


        
