#Line structure of PYTHON
#A logical line is constructed from one or more physical lines Followed by  the explicit or implicit line joining rules.
# -*- coding: <UTF-16> -*-
#NOTE:comments in PYTHON starts with hash character(#)but these are not strings
#Logical lines and physical lines
if 20>4:print('hello')
year=int(input('enter the value of year:'))
month=int(input('enter the value of month:'))
day=int(input('enter the value of day:'))
hour=int(input('enter the value of hour:'))
minute=int(input('enter the value of minute:'))
second=int(input('enter the value of second:'))
#Explicit Line joining using backslash to joing physical lines into logical lines
#after backslash comment is invalid and not allowed
if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
        print('hello')
        print('this is Explicit Line Joining')
        pass
#Explicit line joining:using paranthesis or square or curly brackets as list,dictionaries of data collections
#implicit lines can carry comments
names=['name1','name2','name3',
       'name4','name5','name6',
       'name7','name8','name9']
print(names)
print('this is implicit line joining')

