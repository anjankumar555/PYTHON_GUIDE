#Assert Statements: Assert statements are a convenient way to insert debugging assertions into a program

#Assertions are statements that assert or state a fact of True confidently in program

#In python, these are buitin statements to use to check assertion Condition or Expression which is supposed to True it continues to run the code. If False it raises AssertionError

#AssertionError:it Raised when Assert statement fails

#it is implemented using assert keyword and syntax below

#Syntax: assert expression,[Error Message](or) assert expression1,expression2,expression3,..[Error Message]

#NOTE:Error Message is optional

#Example:

x=2#declaring an object

assert x==2#checking a condition or expression statement if True it continues to next line, else raised error
print(x)#just print x object

assert x==3#condition is false it raised error

print(x)#it raises Assertion Error

#Example AssetionError Message

x='hello world'#declaring an object

#assert x=='Good Morning','x should be hello world'#this is an ErrorMessage
print(x)#now it raises error as ErrorMessage

#example:

x=4;y=7
div=x/y

assert y!=0,'value of y should not be zero'

print(x/y)

#Example:

def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

marks = [55,88,78,90,79]#calling function with list of arguments as positional 
print("Average of mark2:",avg(marks))

marks = []#empty list of arguments as zero positinal arguments
print("Average of mark1:",avg(marks))

