#String and Byte Literals:
#Declaring String Literals:
#strings are enclosed by single or double or triple gives result same.but single or double used for short strings and triple quotes for long stringitems
a='a';a_1='\Program Files';a_2='\n';a_3='WELCOME TO PYTHON';a_4='this is a string literal\n';a_5="WELCOME TO PYTHON";a_6='''WELCOME TO PYTHON''';
a_7=r'this is python';a_8='\newline';a_9=R'literals'
print(a,a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9)
#printing strings with escape sequences:
#printing normal string with single,double and triple quotes return same result.
print('hello world');print("hello world");print('''hello world''')
#declaring strings with prefix and string escapesequeces:
#prefix 'r' or 'R' means rawstring or rawdata or plain English Language, but it is optional in string and bytes literals.
print(r'hello world');print(R'hello world');
#prefix 'u'or 'U' indicates english along with any other language like 'telugu' language, etc.
print(u'మీరు ఎలా ఉన్నారు');print(U'మీరు ఎలా ఉన్నారు');print(U'మీరు ఎలా ఉన్నారుhow are you123')
#prefix with escapesequeces:
print(r"\"hello world")
print('hello world\newline')#here backslash and newline is ignored,so that it is printed as 'ewline' in nextline after 'hello world'.
print('hello world\\')#it prints string after backslash.
print('hello world\f')#it prints ASCIIformfeed after string.
print('hello world\b')#it prints ASCIIbackspace after string.
print('hello world\a')#it prints ASCIIbell after string.
print('hello world\n')#it prints ASCII linefeed aftersting.
print('hello world\r')#it prints ASCII carriage return.
print('hello world\t')#it prints ASCII horizontal tab.
print('hello world\v')#it prints ASCII vertical tab.
print(u'మీరు ఎలా ఉన్నారుh0o2429\ooo,0o3439')
print(U'మీరు ఎలా ఉన్నారుa3f\Xhh')
#print(U'మీరు ఎలా ఉన్నారు\N{ఎక్కడ}')
#Declaring Byte Literals:
print(b'hello')
print(rb'hello world\u')
print(u'hello')
print('hello world\nwelcome to world')

