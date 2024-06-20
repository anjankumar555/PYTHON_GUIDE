#Compound Statements in Python:
#NOTE4:IF clause used for conditional execution.
#IF,WHILE,FOR,TRY,WITH,FUNCTION and CLASS definition are compound statements.
#NOTE1:IF,WHILE and FOR start with name followed by colon(:)which specify indentation and controls block of code or statements.
#IF-clause:1 TAB or 4 SPACES.
#NOTE2:IF clause first evaluates condition,later condition is TRUE then executes block of code or statements.
#An operation or expression is followed by IF clause is called Condition or Test.
if 1>0:#here condition is always followed by IF clause.
    print('block of code success')#Block of Code
if 0>1:#here this condition is FALSE
    print('block of code unsuccess')#it can't execute.
if 1>0: print('hello')#single line
if 2>1<3>2:#Checking any number of operands in oneline.
    print('block of code success2')
#NOTE:any number of conditions checking using IF clause is called Nested-IF clause,but in this case all conditions should be TRUE then only execute a block of code or statements.
#Nested-IF:more than one IF clause and conditions,it checks all conditions then code executed.
if 1>0:#comparision expression
    if 2<<1!=False:#shifting expression
        if (4%2==0):#arithmetic expression
            if any([1,2,3,4]):#built-in functions
                if 1 in [0,1,2,3,4]:#membership expressions
                    if (1&2^3|4!=None):#Bitwise expressions
                        if 1 and 2 or 3!=1:#Boolean expressions
                            if 2+2==4:#any kind of operation
                                if 2*3==6:#comparision expression
                                    print('Nested IF clauses success')#all conditions must be TRUE.so that block of code executed successfully.
#NOTE:without indentation,syntax of conditional expression.
print('IF-ELSE in oneline:')
print('hello world' if 1>0 else 'unsuccess')#first evaluates condition,it return block of code if TRUE.
#NOTE:IF-ELSE execute block of code which condition evaluates TRUE.
print('IF-ELSE clause:')
if 2==2:
    print('code of statements executed')
else:
    print('unsuccessful')
#NOTE:it executes only one block of code which condition evaluates TRUE.
print('IF-ELIF-ELSE:')
if 1>0:#TRUE
    print('positive number')
elif -1<0:#block exit,not checking the condition because above condition TRUE then it out of indentation.
    print('negative number')
else:#No condition should apply
    print('undefined')
#NOTE:Nested IF-ELSE execute block of code which condition evaluates TRUE and all conditions FALSE,then ELSE executed.
print('Nested-IF-ELSE clause:')
if 2!=2:
    print('code of statements executed1')
if 2%2==1:
    print('code of statements executed2')
if 3//2==0:
    print('code of statements executed3')
if pow(2,4)==16:#built-in functions in clause.
    print('code of statements executed4')#TRUE
else:#No condition
    print('unsuccessful')

print('Nested IF-ELIF-ELSE:')
if 1<0:#FALSE
    print('positive number')
elif -1>0:#FALSE.
    print('negative number')
elif 1 not in [0,-1,2,4,5,6,7]:
    print('sucess code')
else:#No condition should apply and all conditions FALSE,this block of code executed.
    print('undefined')                                  
#NOTE:ELSE is always optional in all type of IF clauses and it always use once in the clause.
#NOTE:ELSE  should not contain any expression part and it will executed when all conditions FALSE.
#CASE1:IF-clause
if 1>0:#TRUE
    print('block of code1')#executed
if 2>0:#TRUE
    print('block of code2')#execu
#CASE2:Nested-IF clause
if 1>0:#TRUE
    print('block of code1')#executed
if 2>0:#TRUE
    print('block of code2')#executed
if 3>0:#TRUE
    print('block of code3')#executed
else:
    print('unsuccess')#not executed and it is always optional.
#CASE3:IF-ELIF-ELSE
if 1>0:#TRUE
    print('block of code1')#executed
elif 2>0:#not execute even conditon is TRUE,because it select exactly one of any expression which evaluates TRUE.
    print('block of code2')#executed
elif 3>0:##not execute even conditon is TRUE,because it select exactly one of any expression which evaluates TRUE.
    print('block of code3')#executed
else:
    print('unsuccess')#it is executed when all conditions FALSE in above.
























    
