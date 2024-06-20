#Operators PYTHON
#list of Operators:
#Arithmetic Operators,Relational Operators,Assignment Operators,Logical Operators,Membership Operators,Identity Operators,Bitwise Operators.
print('''+       -       *       **      /       //      %      @
         <<      >>      &       |       ^       ~       :=
         <       >       <=      >=      ==      != '''
      )
#there are approximately 21 operators mostly used in programs.
#Operators performs operation.
#types of operators based on their performance or mode of operation.
#Arthmatic Operators:printed directly using literals.
#addition operation on Numerical Literals
print(1+2,1+2_3+4,0+1_0+1_2_3_4)#declaring with underscores 
print(1+2,1+2+3,1+2+3+4)#the following two addition operation return same result with or without paranthesis.
print((1+2),(1+(2+3)),(1+2+3+4),(1+2)+(3+4))
print(1.56+5.5654,1.143+3.143+2.343,1.23+2.343+4.323+23.342+3.1412,0.00+3)#Float Literals additon without paranthesis
print((1.56+5.5654),(1.143+(3.143+2.343),(1.23+2.343+4.323+23.342+3.1412),((1.23)+(2.343)+(4.323)+(23.342)+(3.1412))))#with parantheses
print(2e34+3e+34,2e-34+1e3,(1.3e+4)+(0.2_3e7+1.232),(1E+1)+(1.45e-1),1E+1)#Exponent Float Addition
print(1+0j+2+1J,1+2J+5j,0+1j+7)#Complex literals addition
print((1+0j)+(2+1j),(1+2j+5J),(1j+6j),(1-2j)+(3+1J),(-1+2j)+(2+1J),(1+2j)+(1+3))
#Addition:String Literals
print('hello'+'world')#String Concatenation.
print('a'+'b'+'c'+'d')
#Bytes literals Addition:
print(b'hello'+b'world')
#Subtraction operation on numerical Literals:
print(1-2,1-2_3-4,1_2_3_5-1_2_3_4)#declaring with underscores 
print(1-2,1-2-3,1-2-3-4)#the following two subtraction operation return same result with or without paranthesis.
print((1-2),(1-(2-3)),(1-2-3-4),(1-2)-(3-4))
print(1.56-5.5654,1.143-3.143-2.343,1.23-2.343-4.323-23.342-3.1412,0.00-3)#Float Literals subtraction without paranthesis
print((1.56-5.5654),(1.143-(3.143-2.343),(1.23-2.343-4.323-23.342-3.1412),((1.23)-(2.343)-(4.323)-(23.342)-(3.1412))))#with parantheses
print(2e34-3e+34,2e-34-1e3,(1.3e+4)-(0.2_3e7-1.232),(1E+1)-(1.45e-1),1E+1)#Exponent Float Subtraction
print((1+0j)-(2+1j),(1+2j-5J),(1j-6j),(1-2j)-(3+1J),(-1+2j)-(2+1J),(1-2j)-(1-3))#Complex literals subtraction
#NOTE1:addition of string with numerical,bytes and unicode literals not allowed.''str'+'str','bytes'+'bytes','unicode'+'unicode'.
#NOTE2:subtraction of string,bytes and unicode literals is not allowed.
#Multiplication operation on numrical literals:
print(1*2,1*2_3*4,1_2_3_5*1_2)#declaring with underscores 
print(1*2,1*2*3,1*2*3*4)#the following two multiplication operation return same result with or without paranthesis.
print((1*2),(1*(2*3)),(1*2*3*4),(1*2)*(3*4))
print(1.56*5.5654,1.143*3.143*2.343,1.23*2.343*4.323*23.342*3.1412,0.00*3)#Float Literals multiplication without paranthesis
print((1.56*5.5654),(1.143*(3.143*2.343),(1.23*2.343*4.323*23.342*3.1412),((1.23)*(2.343)*(4.323)*(23.342)*(3.1412))))#with parantheses
print(2e34*3e+34,2e-34*1e3,(1.3e+4)*(0.2_3e7*1.232),(1E+1)*(1.45e-1),(1E+1)*2)#Exponent Float multiplication.
print((1+0j)*(2+1j),(1+2j*5J),(1j-6j),(1-2j)*(3+1J),(-1+2j)*(2+1J),(1-2j)*(1-3))#Complex literals Multiplication.
#Multiplication on string literals with numerical literals:
print('hello world'*3);print(3*'hello world')#it prints 3 times as given string.
print(b'hello python'*2);print(2*'hello python')# it prints 2 times as given bytes.
#Multiplication for LIST,TUPLE:
print(4*[2])#it prints 4 times list
print(3*[1,2,3])#it prints 3 times
print(2*[1,2,3,4,'a','python'])
print(3*(1,2,3))#it prints 3 times tuple.
print(0*(1,2))#empty TUPLE.
print(None*[1])
#NOTE:Multiplication not allowed for SET,DICT.
#NOTE3:multiplication of string with string and other literals not allowed.
#NOTE4:multiplication of string,bytes and unicode must be with integer literals.
#Division operation on numerical literals:
print(1/2,12_3/4,1_2_3_5/1_2)#declaring with underscores 
print(1/2,1/2/3,1*2*3*4)#the following two division operation return same result with or without paranthesis.
print((1/2),(1/(2/3)),(1/2/3/4),(1/2)/(3/4))
print(1.56/5.5654,1.143/3.143/2.343,1.23/2.343/4.323/23.342/3.1412,0.00/3)#Float Literals division without paranthesis
print((1.56/5.5654),(1.143/(3.143/2.343),(1.23/2.343/4.323/23.342/3.1412),((1.23)/(2.343)/(4.323)/(23.342)/(3.1412))))#with parantheses
print(2e34/3e+34,2e-34/1e3,(1.3e+4)/(0.2_3e7/1.232),(1E+1)/(1.45e-1),(1E+1)/2)#Exponent Float division.
print((1+0j)/(2+1j),(1+2j/5J),(1j-6j),(1-2j)/(3+1J),(-1+2j)/(2+1J),(1-2j)/(1-3))#Complex literals division.
#NOTE5:division with string,bytes and unicode literals not allowed.
#Modulus operation on numerical literals:
#Modulus operator returns remainder after division.
print(1%2,12_3%4,1_2_3_5%1_2)#declaring with underscores 
print(1%2,1%2%3,1%2%3%4)#the following two modulus operation return same result with or without paranthesis.
print((1%2),(1%(2%3)),(1%2%3%4),(1%2)/(3%4))
print(1.56%5.5654,1.143%3.143%2.343,1.23%2.343%4.323%23.342%3.1412,0.00%3)#Float Literals Modulus without paranthesis
print((1.56%5.5654),(1.143%(3.143%2.343),(1.23%2.343%4.323%23.342%3.1412),((1.23)%(2.343)%(4.323)%(23.342)%(3.1412))))#with parantheses
print(2e34%3e+34,2e-34%1e3,(1.3e+4)%(0.2_3e7%1.232),(1E+1)%(1.45e-1),(1E+1)%2)#Exponent Float Modulus.
#NOTE6:Modulus operation is on complex literals not allowed but only on integer,float,exponent.
#Power operation on numerical literals:
print(1**1,2**2,1_0_0_0**1,0_0**1)#declaring with underscores.
print((1**100),(12**12),(4**1**2**1))#integer to powers of integers.
print((1.2**2.0),(1.23**1.23**2.00))#float powers.
print((2E-34)**2),((3.2e+1)**3),((1e2)**0.76),(1.1213)**2e1,(1.1413)**1.1413e2#exponent powers to the base exponent literals.
print((1+2j)**3,(1.23+.34j)**2,(0.87+1.23j)**1.23,(1.12E2+2j)**1.3e2,(1.323+0.23e-1j)**0.34)#imaginary exponent
#NOTE7:Power operation is not allowed for other literals except numerical.
#Floor division operation on numerical. 
#NOTE8:Floor division(//) returns integer value after division.
print(12_2_3//4,1_0_0_0//3_2,1_2_1_4//7_1)# on integer literals with underscores.
print(1231//33,23424//332,1212//4,564//8,(564)//8,(1231)//33)#with paranthesis and without.
print(1.23//0.23,453.22//54.9,424.44//1.2232)#float literals
print(2e1//3,1.23E+2//1.342,0.453e-5//2e23,2e12//1.3E-1)#Exponent literals floor division.
#NOTE8:Floor of complex literals not allowed.
#ARITHMETIC CONVERSIONS:
print(1+(2+3j),1-(2-3j),2*(2+3j),1/(2+3j))#complex with other literal is result complex.
print(1+1.2323,2-1.23,3*1.1413,2/1.232,343%3.2324)#float with other literal is result float.

