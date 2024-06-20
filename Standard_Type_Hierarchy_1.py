#Here Standard Type Hierarchy is a list of types discussed below one by one:

#1.Numbers: These are created by numeric literals but python distinguishes Numeric Literals From Numbers(Buit-in module)also

#Numbers are Integers, Float point Numbers and Complex Numbers

#Integers: 1.Integers 2. Bool

#Note:#Integers in unlimited range supported by python

#Integers:Generally as per mathematical standards integers may be positive and negative ...-3,-2,-1,0,1,2,3,..... all supported in python

#Note:Negative Integers are represented by 2's complement of positive number

x=1;y=1000;z=1000000#these are integer objects
a=-1;b=-1000;c=-100000#these are negative integers

print(type(x));print(type(y));print(type(z))#all are actually Integer classes, so that here 1,10,100000 are objects of type Integers. then based on type of data, their attributes and methods assigned automatically as shown below

#Special Attributes: These are started with 2 underscore and ending with 2 underscores, but they are not intended for general use like methods.

print(x.as_integer_ratio);print(x.bit_length);print(x.conjugate);print(x.denominator);print(x.from_bytes);print(x.imag);print(x.numerator);print(x.real);print(x.to_bytes)#similarly for y and z also

#Special Attributes: Object attributes as behaviours
print(x.__abs__)
print(x.__add__)
print(x.__and__)
print(x.__bool__)
print(x.__ceil__)
print(x.__class__)
print(x.__delattr__)
print(x.__dir__)
print(x.__doc__)#it returns functions documentation as String, If not available then returns None. but not inherited by subclasses
print(x.__setattr__)
print(x.__eq__)
print(x.__float__)
print(x.__floor__)
print(x.__floordiv__)
print(x.__format__)
print(x.__ge__)
print(x.__getattribute__)
print(x.__getnewargs__)
print(x.__gt__)
print(x.__hash__)
print(x.__index__)
print(x.__init_subclass__)
print(x.__int__)
print(x.__invert__)
print(x.__le__)
print(x.__lshift__)
print(x.__lt__)
print(x.__mod__)
print(x.__mul__)
print(x.__ne__)
print(x.__new__)
print(x.__or__)
print(x.__pos__)
print(x.__pow__)
print(x.__radd__)
print(x.__rand__)
print(x.__rdivmod__)
print(x.__reduce__)
print(x.__repr__)
print(x.__rfloordiv__)
print(x.__rlshift__)
print(x.__rmod__)
print(x.__rmul__)
print(x.__ror__)
print(x.__round__)
print(x.__rpow__)
print(x.__rrshift__)
print(x.__rshift__)
print(x.__rsub__)
print(x.__rtruediv__)
print(x.__rxor__)
print(x.__sizeof__)
print(x.__str__)
print(x.__sub__)
print(x.__subclasshook__)
print(x.__truediv__)
print(x.__trunc__)
print(x.__xor__)

#Booleans: These represents Truth values: True and False. these are also objects only under Bool Class.

#Note: True stands for 1 and False stands for 0. Integers type

print(bool(1));print(bool(0))

print(bool(100));print(bool('hello world'))#it checks Truth values for String objects also

print(bool(0000));print(bool(2+3));print(bool(~(100010)));print(bool(~(00000)))#Even for binary numbers and arthmetic operations

#2.Real or Float Numbers: these are float numbers divided in 2 types:

#1.Float point numnbers: these fractional numbers or decimal

x_1=1.1413;y_1=0.707;z_1=-1.1413#these are float point Objects under Float Class
print(type(x_1));print(type(y_1));print(type(z_1))#type of data objects and values

#2.Exponent Numbers: these are kind of Float point numbers

x_2=1e23;y_2=-1e34;z_2=1.2e23#exponent objects 

print(type(x_2));print(type(y_2));print(type(z_2))#Float Classes only

#Note:Based on the type of value object, attributes and methods may have changes.

print(x_2.as_integer_ratio);print(x_2.conjugate);print(x_2.fromhex);print(x_2.hex);print(x_2.imag);print(x_2.is_integer);print(x_2.real)#thsse are methods of exponent 

#Note:these are also have same  object attributes and methods like Integer above

#3.Complex Numbers: these are pair of Real and Imaginary parts of numbers

x_3=1+1j;y_3=1-0j;z_3=-1-1j;z_3_1=1e2+1.2e3j

print(type(x_3));print(type(y_3));print(type(z_3));print(type(z_3_1))#Complex Class of Numbers

print(x_3.conjugate);print(x_3.imag);print(x_3.real)#it has only these methods objects based on their type. but attributes are same like integers
