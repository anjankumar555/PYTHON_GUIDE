#Control Flow Statements:While
#WHILE:it is used for repeated execution as long as condition is TRUE.
#Syntax:
#NOTE1:WHILE is continuously or repeatedly executed the block of code when expression is TRUE.
#NOTE:WHILE allows any kind of expressions not only comparision
#CONTINUE,BREAK statements optional
print('WHILE statement:')
while 3<5:#TRUE,so it repeatedly executes block of code.
    print('block of code repeated successfully')
    break
else:#loop is terminates because above condition is TRUE,not execute else part.
    print('unsuccess')
#NOTE:To stop repeatedly execute the block of code,BREAK statement is used.and is terminates loop without executing else part.
#NOTE:BREAK only occur in nested WHILE.
print('WHILE statement:')
while 3<5:#TRUE,so it repeatedly executes block of code.
    print('block of code repeated successfully')
    break#Terminates the loop and executes block of code without executing else block of code.
else:#loop is terminates because above condition is TRUE,not execute else part.
    print('unsuccess')
#NOTE2:CONTINUE statement is used for continue the execution, skips rest of the suite and goes back to testing condition.it continues with next cycle of nearest loop.
print('WHILE statement:')
while 3<5:#TRUE,so it repeatedly executes block of code.
    print('block of code repeated successfully')
    break#this loop is completed by BREAK statement.
else:#loop is terminates because above condition is TRUE,not execute else part.
    print('unsuccess')
print('Nested-WHILE statements:')
while 2<4:
    print('block of code repeated successfully2')
    break#it breaks execution flow,so it executes only once.
while 3>1:
    print('block of code repeateed successfully3')
    break#it breaks execution flow,so it executes only once.
while -1<0:
    print('block of code repeateed successfully4')
    break
while pow(2,3)==8:#math functions
    print('block of code repeateed successfully5')
    break
while any([1,2,3,4,5])==True:#built-in functions
    print('block of code repeateed successfully6')
    break#terminates nearest enclosing loop.
#NOTE:ELSE clause is always optional in all type of WHILE clauses.
#CASE1:
while 3>5:
    print('hello')
    continue#it always goes back to test condition and skips rest of statements
else:
    print('unsuccess')
#CASE2:
while 2<1:
    print('hello1')
    break
while 3>2:
    print('hello continue')
    break
#CASE3:Nested-WHILE without BREAK.
while 3<2:#FALSE
    while 4>5:#FALSE
        continue#Terminates loop because testing the condition.
    while 1>0:#TRUE
            print('continue')#not execute,because above conditions FALSE.
            continue#it continues with next cycle of nearest loop.
#CASE4:WHILE-IF
print('WHILEE-IF:')
while 3>2:#it test condition and executes entire loop,till the BREAK statement.
    if 4%2==0:#TRUE
        print('block of statements1')
    if 5>4:
        print('block of statements2')
    if 4%2==0:
        print('block of statements3')
        break#Breaks loop
    break#terminates whole loop.
#CASE:
while 3>2:
    print('first block of code')#it executes only once if block of code present and terminate loop from other part like IF,ELSE etc.
    break#it terminates loop,so it cant execute next cycle.
    if 4%2==0:#not allows next cycle.
        print('block of statements1')
    if 5>4:
        print('block of statements2')
        break
    if 4%2==0:
        print('block of statements3')
#CASE5:Nested-WHILE-IF:4 claused 4 break statements to terminate nearestloop.
while 9 in [1,2,0,9,99,999]:
    while any([1,2,3,4])==True:
        if 5>4:
            if 2.5e32>1:
                print('Nested While-IF')#repeated execution in console even one break use 
                break#first loop
            break#second loop
        break#third loop
    break#last loop
#CASE:IF-WHILE
if 31%2!=0:
    while 3>2:
        print('IF-WHILE loop starts')
        break
#CASE:
while 4>3:
    print('code1')
    break
while 5>4:
        print('code2')
        break#repeated execution above 2 even use BREAK statement.
    #repeated next cycle of nearest loop.
#CASE:
while 4>3:
    print('code1')
    while 5>4:
        print('code2')
        break
    continue#repeated execution entire loop.
    #continue testing back condition and repeated next cycle of nearest loop.
#CASE:
while 4>3:
    print('code1')
    while 5>4:
        print('code2')#this codea2 is repeated.
        continue#it continues with next cycle of nearest loop.
    continue#repeated execution entire loop.
#NOTE:Boolean values used directly in loop.
while(True):
    print('Hello')#it executes until TRUE and breaks 
    break
while(False):
    print('Hello')#it not executes untill TRUE.
    continue



