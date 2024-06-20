#Expression Statements: Expression Statements are used mostly interactively to compute value and write a value or usually to call a procedure which returns no meaningful result

#Expression Statement evaluates the Expression list which may be a single Expression

#In Interactive Mode, any value or statement except None, is converted into String by using repr()built-in function and printed on line by itself

#NOTE:An Expression Statement is simply a expression or expression statements

#Examples:

print(1)#to write a value 
print(123)#to write a value as a statement
print('hello')#expression statement as a string

print(1+2+3+4)#to compute a value 
print((1+2)*(3+4))#to compute a value

#NOTE: above code prints value as expression statements into string on console using repr() built-in function

q=[1+2,2+3,3+4,4+5,6-5,7-8,(1*3)+4,8,0+0]#expression statements
print(q)
print(2*[1,2,3,4,5])#it returns each item 2 times in list 

print((1+2+3,4,6*4,4-3,5+0))#Tuple of expression statements


#repr():Buit-in Function return a string containing a printable representation of an object
print(repr(1))#it returns string same as expression statement
print(repr('hello'))
print(repr(1.1413));print(repr(1+2j))#it converts into printable string object 
