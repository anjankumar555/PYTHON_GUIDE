#Demonstrating Comparision Operators
#List of Comparision Operators:
print('COMPARISON OPERATORS:')
print(''' <    >    ==  'IS' 'ISNOT' 

          <=    >=     !=  = 
          ''')
#comparision between integers.
#it compares the values on left and right side and  returns boolean values:'True' or 'False' always.
print('INTEGERRS:')
print(0<1,1<2,2<3,3<4,4<5)#it returns boolean values.
print(1>0,2>1,3>2,4>3,5>4)#it returns boolean values,these are
#NOTE:X==Y implies X is Y.
print(0==0,1==1,2==2,3==3,4==4)#True if left and right values same or else False.
print(1==0,0==1,2==3,3==2,4==5)#True if left and right values same or else False.
print(0<1,0>1)#it means the same.
print(1!=2,3!=4,5!=34,143!=1.43)#True if left and right values same or else False.
#'ISNOT' and != means same.
#1 is not 1,2 is not 2,34 is not 56,111 is not 1111,76 is not 67,33 is not 34:#True if left and right values are not same or else False.
#AND operation:
print('AND OPERATION:')
print(0<=1)#in this case 0 is less than 1 and it returns True but 0 is equal to 1 returns False.so finally 'True' and 'False' = 'True'.
print(-1>=2)#in this case -1 is not greater than 2 returns False and not equal to 2 returns False.sa finally 'False' and 'False' = 'False'.
#NOTE_0:'AND' operation:
#T AND T=T
#T AND F=T
#F AND T=T
#F AND F=F
#NOTE0:'AND' operation inside operation,if more than one comparision operator presents and even in chain process.
print(1<2<=3)#here 1<2 returns True and 2<3 returns True,2 is not equal to 3 returns False.so (True and (True and False))=='True'.
print(0<=1,1<=2,2<=3,3<=4,4<=5,5<=6,6<7)
print(1>=0,2>=1,3>=2,4>=3,5>=4,6>=5,7>=6,8>=7)
#Comparision between float literals.
print('FLOAT LITERALS:')
print(0.0<1.0,1.0<2.0,2.0<3.0,3.0<4.0,4.0<5.0)#it returns boolean values.
print(1.0>0.0,2.0>1.0,3.0>2.0,4.0>3.0,5.0>4.0)#it returns boolean values.
print(0.0==0.0,1.0==1.0,2.0==2.0,3.0==3.0,4.0==4.0)#True if left and right values same or else False.
print(1.0==0.0,0.0==1.0,2.0==3.0,3.0==2.0,4.3==5.6)#True if left and right values same or else False.
print(0<1,0>1)#it means the same.
print(1.9!=2.8768,3.756!=4,5.87!=34.34,143!=1.43)#True if left and right values same or else False.
#Exponent Literals.
print('EXPONENTIAL LITERALS:')
print(0<0e0,1<1e23,32<1e-3,43<242e+32,4<34e2)
print(2e23>23e4,1e34>434e2,1e34>4e-44,1e+443>34e-32)
print(1.23e3>=8.34e2,32.232>=7.3e45,2.3e2<=54e+6)
print(1e2<=0e2,1.2e3<=54.343,6.3e-43<=4e-82)
print(0e0==0e0,1e2==2e3,1.2e3==3.45e3,0.45e3==0.12)
print(1e3!=34,42.4e-5!=0.8e-233,34e-2!=1.32e4)
#Complex Literals:
print('COMPLEX LITERALS:')
print(1+1j==1+1j,2+3j==4+1j,1.2+5.3j==5.8+45j)
print(1.2e-3+3.45j!=1.23+0.45e-4j,1.34+5j!=3.14e+32+1.4e56j)
#NOTE1:'<' '>' '<=' '>=' are not supported for complex literal values.
#NOTE2:Comparisions can be chained arbitrary.
print('COMBINATIONS:')
#NOTE:Comparision should be transitive.
print(1<2)#not 2>=1,it applies to totally ordered collections like LIST only.
print(2>1)#not 2<=1,it applies to totally ordered collections like LIST only.
print(1<2<=3)#not 1>=3.
print(1>2>=3)#INVERSE COMPARISION.
print(1<2<3<4<5)#we can compare any number of values in one line.
print(1<2<3)#it implies 1<3
print(1<2<=3)#it implies 1<3
print(5>4>3>2>1)#it means 5>4 and 4>3 and 3>2 and so on....
print(5>4>3>2>=1==1!=0>=-1)#combination of operators.
print(9>7>4<8>5<100>-1>-100<-1.1413!=2.343)
print(23>33<43.232>56.987>=87.121<=143.23>-23.32<-1000.33>=2<-1.232<=-0.232==1!=0.9999)
print(1<2<3)#1 less than 2 and 2 less than 3 but no comparision between 1 and 3.
print(1<2>3)#legal.





