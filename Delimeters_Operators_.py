#To demonstrate Delimeters.
#list of delimeters used throughout the program.
print('PYTHON DELIMITERS:')
print('''  (       )       [       ]       {       }
            ,       :       .       ;       @       =       ->
            +=      -=      *=      /=      //=     %=      @=
            &=      |=      ^=      >>=     <<=     **=   '''
      )
#Brackets:
print('usage of brackets:')
print('Brackets are used for defining arguments in built-in functions like PRINT,ANY,ALL etc..')
print('Brackets are used for declaring Datacollections:SET,FROZENSET.')
print((1,2,3,4,5,6,7,8,9,0))#SET object.
#Square Brackets:
print('Usage of Squarebrackets')
print('these are used for defining optional arguments in functions')
print('Brackets are used for declaring Datacollections:LIST')
print([1,2,3,4,5,6,7,8,9,0,'a','A','python','$'])#LIST object.
#Flower brackets:
print('Usage of flower brackets:')
print('Unlike C,these are used for declaring Datacollections:DICTIONARY')#not for conditional statements like IF,WHILE,etc..
print({1:'a',2:'A',3:'PYTHON',4:'java oops',5:100})#DICTIONARY object.
#Comma:
print('Usage of Comma operator:')
print('Comma generally used to seperate elements,objects,arguments,identifiers,literals etc..')
print('python','java','apple','orange')#Strings seperated by comma.
print(1,1.23,12e+34,1e-34,1e4143,1+3j,12e3+3e+425j)#Numeric Literals seperated by comma.
a=1;b=2
print(a+b)#Identifiers
print([1,2,3,4,5,6,7,8,9,0,'a','A','python','$'],(1,2,3,4,5,6,7,8,9,0),{1:'a',2:'A',3:'PYTHON',4:'java oops',5:100})#LIST,TUPLE,SET,DICTIONARY etc...
print([0,1,2,3,4,1.23])#ARRAY object.
#Colon:
print('usage of colon')
print('colon used for declaring KEY-VALUE pairs in the Dictionary object.')
print({1:'a',2:'A',3:'PYTHON',4:'java oops',5:100})#DICTIONARY
print('Datascience programming Language:PYTHON')#Strings purpose also like Headlines.
#Dot operator:
print('Usage of dot operator:')
print('generally it is called  Embedded operator in PYTHON')
print('Because of it is used for Name and Binding the methods and give access to writing a code')
print('it is widely used in OOPS Concept,Attributes of objects')#if we use dot,it is method to access submodules.
a=1;b=2;c='python';d=1.23#a,b are integer objects and c is string object.
print('we can access Attributes and special methods of objects given below:')
print(a.real,b.imag,a.bit_length,a.conjugate,b.conjugate,b.real,a.denominator,a.numerator,a.from_bytes,a.imag,a.to_bytes)#Attributes of a object accessed and b as well.
print(a.__abs__,a.__add__,a.__class__,a.__pow__,a.__ceil__,a.__floordiv__,a.__dir__,a.__floor__,a.__format__,a.__getattribute__,a.__rshift__,a.__init__,a.__dir__,d.real,d.fromhex)#Special methods of objects accessed using dot operator and it returns object
#Is Equal to operator:
print('Usage of = operator')
print('it is quite different from (==) comparision operator')
print('it is generally assigning values to objects,identifiers,literals Etc..')
print('it is assigning values to objects')
a=10;b=20;c=1.23;d=12e34;e=1e-56;f=1+2j;h=1.23+4.5j;j=12e4+3e-3j;k='python'
print(a,b,c,d,e,f,h,j,k)#assigning values to identifiers.
#Semicolon:
print('Usage of semicolon operator:')
print('it is generally used to seperate variables or identifiers or strings,Bytes')
a=10;b=20;c=1.23;d=12e34;e=1e-56;f=1+2j;h=1.23+4.5j;j=12e4+3e-3j;k='python'
print(a,b,c,d,e,f,h,j,k)#assigning values to identifiers.
#Addition and isEqual to(+=):
#NOTE:it means first addition and assigning value to that object.
#NOTE:String concatenation is also allowed.
print('this operator used for additon and assigning result value to that object')
a=1_0;b=2_0;c=1.2_3;d=1_2e34;e=1e-5_6;f=1+2j;h=1.2_3+4.5j;j=1_2e4+3e-3j;a_1='python'#values of objects.
a+=1_0;b+=2.3_4;c+=12e3_4;d+=1+2j;e+=1e2_3+1.2e4_5j;f+=12.3e43;h+=1e-1;j+=2.3e+407;a_1+='language'#addition and assigning values to actual values.
print(a);print(b);print(c);print(d);print(e);print(f);print(h);print(j);print(a_1)#final printing result after assigning
#Subtraction and isEqual to(-=):
#NOTE:it means first subtraction and assigning value to that object.
print('this operator used for subtraction and assigning result value to that object')
a=1_0;b=2_0;c=1.2_3;d=1_2e34;e=1e-5_6;f=1+2j;h=1.2_3+4.5j;j=1_2e4+3e-3j;a_1='python'#values of objects.
a-=1_0;b-=2.3_4;c-=12e3_4;d-=1+2j;e-=1e2_3+1.2e4_5j;f-=12.3e43;h-=1e-1;j-=2.3e+407#addition and assigning values to actual values.
print(a);print(b);print(c);print(d);print(e);print(f);print(h);print(j)#final printing result after assigning
#Multiplication and isEqual to(*=):
#NOTE:it means first Multiplication and assigning value to that object.
#NOTE:String multiplication with integers is also allowed.
print('this operator used for multiplication and assigning result value to that object')
a=1_0;b=2_0;c=1.2_3;d=1_2e34;e=1e-5_6;f=1+2j;h=1.2_3+4.5j;j=1_2e4+3e-3j;a_1='python'#values of objects.
a*=1_0;b*=2.3_4;c*=12e3_4;d*=1+2j;e*=1e2_3+1.2e4_5j;f*=12.3e43;h*=1e-1;j*=2.3e+407;a_1*=2#addition and assigning values to actual values.
print(a);print(b);print(c);print(d);print(e);print(f);print(h);print(j);print(a_1)#final printing result after assigning
#Division and isEqual to(/=):
#NOTE:it means first Division and assigning value to that object.
print('this operator used for division and assigning result value to that object')
a=1_0;b=2_0;c=1.2_3;d=1_2e34;e=1e-5_6;f=1+2j;h=1.2_3+4.5j;j=1_2e4+3e-3j#values of objects.
a/=1_0;b/=2.3_4;c/=12e3_4;d/=1+2j;e/=1e2_3+1.2e4_5j;f/=12.3e43;h/=1e-1;j/=2.3e+407#addition and assigning values to actual values.
print(a);print(b);print(c);print(d);print(e);print(f);print(h);print(j);print(a_1)#final printing result after assigning
#FloorDivision and isEqual to(/=):
#NOTE:it means first FloorDivision and assigning value to that object.
print('this operator used for floordivision and assigning result value to that object')
a=1_0;b=2_0;c=1.2_3;d=1_2e34;e=1e-5_6;j=1_2e4#values of objects.
a//=1_0;b//=2.3_4;c//=12e3_4;d//=1e345;e//=1e2_3+1.2e4_5;j//=2.3e+407#addition and assigning values to actual values.
print(a);print(b);print(c);print(d);print(e);print(f);print(h);print(j)#floordivision returns always integer only and it is not supported for complex.
#Modulus and isEqual to(/=):
#NOTE:it means first Modulus and assigning value to that object.
print('this operator used for Modulus and assigning result value to that object')
a=1_0;b=2_0;c=1.2_3;d=1_2e34;e=1e-5_6;j=1_2e4#values of objects.
a%=1_0;b%=2.3_4;c%=12e3_4;d%=1e345;e%=1e2_3+1.2e4_5;j%=2.3e+407#addition and assigning values to actual values.
print(a);print(b);print(c);print(d);print(e);print(f);print(h);print(j)#floordivision returns always integer only and it is not supported for complex.
#Power and isEqual to(/=):
#NOTE:it means first Power and assigning value to that object.
print('this operator used for Power and assigning result value to that object')
a=1_0;b=2_0;c=1.2_3;d=13.4;e=0.6;f=1+2j;h=1.2_3+4.5j;j=4+3e-3j;a_1='python'#values of objects.
a**=1_0;b**=2.3_4;c**=1.24;d**=1j;e**=1.2e4_5j;f**=2.33;h**=1e-1;j**=2.3#addition and assigning values to actual values.
print(a);print(b);print(c);print(d);print(e);print(f);print(h);print(j)#final printing result after assigning.
#Colon and isEqual to(:=):
#NOTE:it means first Colon and assigning value to that object.
print('this operator used for colon and assigning result value to that object')
a_1={1:'a',2:'A',3:'PYTHON',4:'java oops',5:100}
print(a_15:=9)
#BitwiseAND and isEqual to(&=):
#NOTE:it means first BitwiseAND and assigning value to that object.
print('this operator used for BitwiseAND and assigning result value to that object')
a=12;b=2;c=231;d=100#it is only for integers
a&=4;b&=30;c&=6;d&=10
print(a);print(b);print(c);print(d)
#BitwiseOR and isEqual to(|=):
#NOTE:it means first BitwiseOR and assigning value to that object.
print('this operator used for BitwiseOR and assigning result value to that object')
a=12;b=2;c=231;d=100#it is only for integers
a|=4;b|=30;c|=6;d|=10
print(a);print(b);print(c);print(d)
#BitwiseXOR and isEqual to(^=):
#NOTE:it means first BitwiseXOR and assigning value to that object.
print('this operator used for BitwiseXOR and assigning result value to that object')
a=12;b=2;c=231;d=100#it is only for integers
a^=4;b^=30;c^=6;d^=10
print(a);print(b);print(c);print(d)
#Rightshift and isEqual to(<<=):
#NOTE:it means first Rightshift and assigning value to that object.
print('this operator used for Rightshift and assigning result value to that object')
a=12;b=2;c=231;d=100#it is only for integers
a<<=4;b<<=30;c<<=6;d<<=10
print(a);print(b);print(c);print(d)
#Leftshift and isEqual to(>>=):
#NOTE:it means first Leftshift and assigning value to that object.
print('this operator used for Leftshift and assigning result value to that object')
a=12;b=2;c=231;d=100#it is only for integers
a>>=4;b>>=30;c>>=6;d>>=10
print(a);print(b);print(c);print(d)
#Other operators:'$','?' these are not using anywhere in PYTHON.
print(10 not 100) 


















