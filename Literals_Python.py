#PYTHON Literals:Literals are builtin type data given to identifiers.
#NOTE:Literals mainly 3 types:String,Bytes and Numerical Literals.
#Demonstrating the literals
#Literals:Constant values of some built-in types like integer,float,character,boolean,bytes and strings etc...
#Literals numeric and string types.
#defining Numeric Literals:Integer numbers,Float numbers,Complex numbers.
#Note:Numeric Literals should not use a sign.
#Types of  integer literals:Decimal,binary,octal and hexa integers
#defining decimal intergers:Nonzero digit
print('DECIMAL INTEGERS:')
a=0;b=1;c=1_2;d=0+1;e=1_2_30;f=1+0
print(a,b,c,d,e,f)
#declaring binary integers:
print('BINARY INTEGERS:0 AND 1 ONLY')
a=0b0011000;b=0B1111000100;c=0b_10010100;d=0b1_0_1_0_1_0;e=0b10_111_000+0B10010_100;f=0b0010
print('0b0011000:',a,'0B1111000100:',b,'0b_10010100:',c,'0b1_0_1_0_1_0:',d,'0b10_111_000+0B10010_100:',e,'0b0010:',f)
#declaring octal integers:
print('OCTAL INTEGERS:0-7')
a=0o123;b=0O231;c=0o_23434;d=0o1_4_5_3;e=0o6_54_3+0O1325;f=0o3333
print(a,b,c,d,e,f)
#declaring hexadecimal integers:
print('HEXADECIMAL INTEGERS:0-9 AND a-f AND A-F:')
a=0x0110340;b=0X4746727;c=0x_54_4_3_2_2;d=0x3_1_4_7_8_9+0X5_8_9_0_6;e=0x013034a33;f=0X3947ABC4;g=0x_3_a_f_4_6;h=0x_a_B_c_D_e_F;i=0X_A_2_4_E_F;g=0xdeadbeef
print(a,b,c,d,e,f,g,h,i,g)
#Types of Floating point Literals:point float and Exponent float
#declaring Floating point Literals:point float
a=1.143;b=1.1_4_3;c=.1_4_3;d=1_2_3.63_45_3_0_7
print(a,b,c,d)
#declaring Exponent Float:
a=1e100;b=.564e6_5;c=e;d=e+1;f=1.143E1_2_3;g=0e0;h=1e-134
print(a,b,c,d,f,g,h)
#Declaring Imaginary Literals:
a=3+2j;b=0+1j;c=2J;d=1-0j;e=1.23+1j;f=1e+3_3+12j;g=1.143E4_1-4J;h=1E04+3.2e7_4j;k=10.j
print(a,b,c,d,e,f,g,h,k)
#NOTE1:digits:0-9
#NOTE2:Underscore is ignored for  determinig numeric values and it occur between digits,after base specifiers like 0B,0O,0X
