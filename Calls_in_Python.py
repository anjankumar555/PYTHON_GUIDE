#CALL: A call calls callable object with possibly empty series of arguments.

# A method or a function or objects having a call() method are callable.

#primaries are user-defined objects or pre-defined 

#Syntax:Primary() or Primary(arguments) or primary(Comprehension)

#NOTE:Positional arguments always must be first while passing arguments in above syntax.

complex()#it is a function with empty series of arguments.
#Here complex is a built-in function

complex(1,-1)#Positional only arguments 
print(complex(1,-1))#it prints or calls callable object.

complex(3, imag=5)#positional or  keyword argument.
print(complex(3, imag=5))#it prints or calls callable object.

foo=[1,2,3,4],5,6,7#it is an arbitrary sequence of positional arguments 

def func(foo, bar=None):#sequence of positional followed by keyword.
    pass
#Here func is a primary and it is a user-defined function.

a=1,2,3,4,5,6,7
def f(*a,**b):#a sequence of positional arguments and keyword arguments.
    pass

