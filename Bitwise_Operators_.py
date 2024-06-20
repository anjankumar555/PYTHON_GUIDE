#Binary Bitwise Operators:
#To demonstrate bitwise operators.
#NOTE:these are different from Boolean operators.
print('LIST OF BINARY BITWISE OPERATORS:')
print('''           'AND:&'
           'OR:|(inclusive OR)'
           'XOR':^(exclusive OR)'
           ''')
#NOTE:for bitwise operations, arguments must be integers only. 
#NOTE_0:'AND' operation:
#T AND T=T  1 AND 1=1
#T AND F=F  1 AND 0=0
#F AND T=F  0 AND 1=0
#F AND F=F  0 AND 0=0
print('AND LOGIC:')
print(1&2)#it means 1 AND 2.
print(-1&1)
print(0&-1)
print(0&1,0 and 1)
print(0&1&2)
print(0&1,1&2,2&3)
print(0&1&2&2)
print(0&-1&-1&-3)
print(1_0_0&1_0_0_0)
print(1&1_4_3&-1_2_3&1_1_1&-1_3_3)
#Bitwise OR:
#T OR T=T  1 OR 1=1
#T OR F=T  1 OR 0=1
#F OR T=T 0 OR 1=1
#F OR F=F  0 OR 0=0
print('OR LOGIC:')
print(1|2)#it means 1 in binary=0001,2 in binary=0010.so (0001)OR(0010)=(0011)==result is 3.
print(-1|1_0)
print(0|-1)
print(0|1,0 and 1)
print(0|1|2)
print(0|1,1|2,2|3)
print(0|1|2|2)
print(0|-1|-1|-3)
print(1_0_0|1_00_0)
print(1|1_4_3|-1_2_3|1_1_1|-1_3_3)
#Bitwise XOR:
#NOTE:XOR operation:
print('XOR LOGIC:')
#T XOR T=F  1 XOR 1=0
#T XOR F=T  1 XOR 0=1
#F XOR T=T  0 XOR 1=1
#F XOR F=F  0 XOR 0=0
print(1^2)#it means 1 XOR 2.
print(-1^1)
print(0^-1)
print(0^1)
print(0^1^2)
print(0^1,1^2,2^3)
print(0^1^2^2)
print(0^-1^-1^-3)
print(1_0_0^1_0_0_0)
print(1^1_4_3^-1_2_3^1_1_1^-1_3_3)
#BITWISE NOT:
print('Bitwise NOT:')
print(~2)#only integers literals allowed.
print(~111)
print(~1,~10,~100,~1000)
#Combinations of operators:
print('COMBINATIONS:')
print(1&2|3^4)
print(-1&-2|-3^-4)
print(-1&2|3^-4)
print((-1&-2)|(-3^-4))
print((-1&-2)|(-3^-4)&(13|-5)|(12&-6^3|12)|(10^-53))
#Shifting Operators:
#NOTE:Arguments in shifting must be Integers.it have lower priority than arthimatic operators.
print('SHIFTING OPERATORS:')
print(2<<3)#left shift by 3 number of bits means:it defines as multiplication with  pow(2,3)=2*(pow(2,3)).
print(2>>3)#right shift by 3 number of bits means:it defines as floor division by pow(2,3)=2//pow(2,3).
print(5>>2)#means floordivision  with pow(2,4)=5//pow(5,2);5//25
print(5//25)
print(-1>>4,-2>>4,-3<<3,-5<<1)
print((2<<4)&(-9&5)&(2<<3))
print(10&20^4^-2^5&-13)
print(12^3|5|-32|-4^10)
print((-1&-2)^(4|10)|(-3^-4))


