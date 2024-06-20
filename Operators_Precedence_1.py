#Operators Precedence or Importance while at runtime.
#All Arthmatic operators have not same priority while on operation.
#Among them 1.parentheses highest precedence(delimetre),2.Powers(Exponentials),3.Division,4.Multiplication,5.Addition,6.Subtraction.
print(((56636//544)%45)**2)#it returns float literal as presence of modulus operator. 
print(1+(4-3)*(1000/100)*(20//2)*(1021%3)**2)#it returns float literal.
print(1+2+3+(4+5+6)-(9-3-2)+(22+5+4))#first parantheses evaluated first and then added remainig from value.
print(3+(2+4+9)+(334+76)-56-12-33-(23-13-7))
print(((3+5+7+4+8+2+6)-(44-13-10-9-5-3-2)))
print((3+5+7)+(4+8+2+6)-(44-13-10-9)-(5-3-2))#when used parantheses values are seperately evaluated.
print((3+2)**4/7)#it evaluates from left to right.addition,power and finally result division.
print((3+42)+(13-8)-(3*4)+(45/9)-(594%8)+(34//5)-(2**4))#it evaluates from left to right.
#power operator:
#NOTE:it binds more than unary operators on its leftside and less than unary operators on its rightside.
#NOTE:operations evaluates from left to right but except power operator presence.
print(3+2-1*2**2)#not from left to right because of power operator high priority while on last.
print(2**2*1-2+1)#it is from left to right.
print((((3+2)-1)*2)**2)#it evaluates from left to right,because of paranthesis priority.
print((((2**2)*1)-2)+1)#it evaluates from left to right,because of paranthesis priority.
#NOTE:if paranthesis is presence in the operation, all are same priority.it means operators in paranthesis give same priority.
#Unary and bitwise operators:
#NOTE:Comparision,Membership,Identity operators have the same precedence and evaluates from left to right operation.
print(5>=4!=0>=1)
print((5>=4)!=0>=1)
print((5>=4!=0>=1))
print(5<=4!=0<=1)
print((5<=4)!=0<=1)
print((5<=4!=0)<=1)
print(1+5-3*4**2>=100)
print((1+5-3)*4**2>=100)
print((((1+5-3*4)**2)>=100))
print(2**2+3-2*4/3<=10)
#Bitwise operators:
print('Bitwise operators precedence:')
print(1&2|3&4^4&5)
print((1&2)|(3&4)^(4&5))
print(1&(2|3)&(4^4)&5)#it returns different from above output.
print((1&2)|(3&4)^(4&5))#same
print(1&2|3&4^4&5|(~3))#just negative sign to output.
print(1&(2|3&4^4)&5)#it returns differnt from above output
#Combinations:
print('Combinations:')
print(1+3&4-2|2*2^2**3)
print(((1+3)&(4-2)|(2*2)^(2**3)))#grouping or paranthesized arguments.
print(1+(3&4-2)|(2*2^2**3))#different output in paranthesis.
#Shifting operators:
#NOTE:shifting operators have lower priority than arithmetic operators.
print('Shifting operators:')
print(1+9-7*2<<2)
print(((1+9-7)*2)<<2)
print(1+9-7*2>>2)
print(1+9-(7*2<<2))
print(2>>3*9-7-2+2)
print(1*100//10+2**2//4*3<<2)
print((1*1_0_0//10+2)**2//4*(3<<2))#first evaluates paranthesis values.
print(1*(10_0//10+2)**(2//4*3<<2))
print(1*1_0_0//1_0+(2**2//4)*(3<<2%1_00))
#Boolean operators:
print('Boolean operators:')
print(1_3+2<17 or 10>3)
print(1_4_3<14_2 and 3<5)
print(not 1<2_3)
#Assignment operators:
print('Assignment operators:')
x=4
x+=10
print(x)#first rightside value evaluated and then assigning.
print({1+2:5*5,3+3:'python'})#Dictionary in operations.
x,y=2,4#right value assigned to identifiers.
print(x,y)
print(2<<3)#2*pow(2,3)
print(2>>3)#2//pow(2,3)
print(5<<2)#2*pow(5,2)
print(5>>2)#2//pow(5,2)























