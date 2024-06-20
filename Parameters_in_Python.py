#PARAMETER: A name entity in a function definiton or a method that specifies an argument that function can accept.

#NOTE:In some cases parameters are arguments. so simply parameter is name and value of the name is an argument.

#SYNTAX:function(name1=value1,name2=value2...)
#In above name1,name2 are parameters and value1,value2 are arguments.

#parameters are 5 kinds:

#1.Positonal or Keyword:it specifies an argument that can be passed either positionally or keyword argument. this is a default parameter.

complex(real=3, imag=5)#real,img are keyword parameters and 3,5 are keyword arguments.
print(complex(real=3, imag=5))#it returns complex number.

complex(3, imag=5)#it contains positional and keword arguments.

range(5)#argument passed in a function
print(range(5))

range(1,10)#positional arguments passed in function
print(range(1,10))

sum(range(10))#passed a value in built-in function.
print(sum(range(10)))

#Parameters within Functions:

def fun():#function definition with empty parameters
    pass
fun()#calling fun

#Single parameter:

def fun1(a):#Single parameter
    return#we can also use return statement, it is optional
fun1(1)#their value

#EXAMPLES:

def fun_1(a,b):# a,b are positoinal parameters
    print('Positional arguments')
    pass
fun_1(1,2)#These are postional arguments passed in function call

def fun_2(a,b=2):#positional or keyword parameter
    print('positional or keyword argument')
    pass
fun_2(1)#already we declare parameter,argument in function definition. so no need of calling argument for b

def fun_3(a,b,c=3,d=4):
    print(a+b+c+d)#operation
    pass
fun_3(1,2)#it returns value.

#NOTE:Positional arguments follows keyword argument.

#2.Positional-only: it can specifies an argument positional only and defined by including a character / after them in parameter list.

#Syntax:function(value1,value2,value3,/,value4,name1=value1,name2=value2)

def fun_4(a,b,c,d,e):#All are positional parameters only in function definition
    print('Postional parameters only')
    pass
fun_4(1,2,3,4,5)#calling their arguments in calling function

def fun_5(a,b,c,d,/,e,f,x=5,y=22):#Positional Only parameters
    print('Postional only')
    pass
fun_5(1,2,3,4,5,6)#only declaring arguments of positional only. so it is called Positional Only parameters.

#3.Keyword-only: it specifies an argument that can be supplied by only keyword.defined by including a *  before them in parameter list.

#Syntax:(value1,value2,*,kwonly1,kwonly2)

def fun_6(a,b,c,*,x_1=23,y_1=32,z_1=45):
    print('Keyword only Parameters')
    pass
fun_6(1,2,3)

#4.Var-Positional or Var-Keyword:it specifies an arbitrary sequence of position arguments can be provided in addition to any postional arguments 
#already accepted by other parameter.it is defined by prepending parameter name with *

#Syntax:(*values,**kwargs)

#NOTE:these are arbitrary sequence of positional or keyword arguments in addition to any positional or keyword arguments already accepted by other parameters.

def fun_7(*args,**kwargs):
    print('Variable Positional or Keyword Parameters')
    pass
fun_7(1,2,3,4,5,6,7,8,9,x=3,y=7,z=8)#Any number of arguments pass in calling function

def fun_8(a,b,c,*args1,x=1,c1=4,**kwargs1):
    print('Variable Positional or Keyword Parameters')
    pass
fun_8(1,2,3,[5,6,7,89,8],[5,78,8,56,0],z1=6,z2=78)#we can pass any number of positional or keyword arguments apart from others which already declared in function def.

#NOTE:Positional arguments must follows Keyword arguments always.

#Parameters are defined by names that appear in function definition. it define what type of arguments a function accept.

#Arguments are values passed to function when calling it.













