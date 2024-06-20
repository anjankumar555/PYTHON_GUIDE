#ATTRIBUTE REFERENCES:it is a primary followed by a period and name.
#SYNTAX: primary.identifier
#here identifier is an attribute name and not the variable name.

#Primary:These are represent most tightly bound operations in language.
#primary ::=  atom | attributeref | subscription | slicing | call

#To demonstrate attribute ref: properties of values are attribute references. these are only literals not strings etc....

value_1=2;value_2=3#Here value_1,value_2 are identifiers, 2 and 3 are values/literals.
print(value_1,value_2)#printed the values on console
print(value_1.as_integer_ratio())#attribute ref of value_1
print(value_1.bit_length())
print(value_1.conjugate())
print(value_2.as_integer_ratio())
print(value_2.bit_length())
print(value_2.conjugate())

#above are integer value types 2,3. so that it has the properties of that object
#finally these are attribute references of that objects.
#thses are built-in methods

#creating a primary  for attribute reference by follow syntax.
#these are Literals properties because primary_1 has a integer value.

#NOTE:primary must evaluate to object of type. so based on object type(interger,float,string,bytes and imaginary)it supports attribute references.

#NOTE:This object is then asked to produce the attribute whose name is an identifier.here identifier is an attribute name and not the variable name.

#NOTE:If any attribute is not found for that type of object(not supportable). it raises error: AttributeError.

primary_1=1#interger object
print(primary_1.as_integer_ratio())
print(primary_1.bit_length())
print(primary_1.conjugate())
print(primary_1.real)

#Imaginary Literals
primary_3=4j
print(primary_3.imag)#it return value of img of imaginary object
print(primary_3.conjugate())#it returns conjugate value of object
print(primary_3.real)


#For string object:
#these are attribute references based on the type of value which assigned to primary.
#Based on type of value/Literal, attribute ref available.
#these are also methods followed by dot operator.getitem

primary_2='hello'#here it is string object. so that it has relevant attributes.
print(primary_2.capitalize())#attribute ref for primary_2
print(primary_2.split())#given string value splited in list format.
print(primary_2.format(4,6))#format method
print(primary_2.center(15,'*'))#attribute ref of string value.
print(primary_2.count('hello'))
print(primary_2.upper())#it returns uppercases of given object.


