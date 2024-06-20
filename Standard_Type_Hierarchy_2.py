#Immutable Sequences in Python: there are 4 types: 1.Numbers 2. Strings 3. Tuples and 4. Bytes

#String is a buit-in String Class

#Strings: A String is a sequence of values that represent Unicode code points

#2.Strings: A string is a group or sequence of Characters in Python and it must  starts with single or double quotes but double quotes recommended

#A string is a Text Sequence Type. so Textual data is handled with string objects

#NOTE: Strings must be enclosed in Single, Double and Triple quotes

#Single Quotes: it allows embedded Double Quotes and Vice Versa

#directly printing Strings 

print('hello world')#it uses for short strings
print('"hello world"')#it uses for short and long strings
print('allows embedded "double" quotes')#if string starts with single and ends with single quotes
print("allows embedded 'single' quotes")#if string starts with double and ends with double quotes
print('''Three single quotes''', """Three double quotes""")#starts and ends with three single quotes or three double quotes
print('''Triple quotes basically used for long string or documentation''')#triple quotes may span multiple lines like paragraphs

#Declaring String objects:
a='a';a_1='\Program Files';a_2='\n';a_3='WELCOME TO PYTHON';a_4='this is a string literal\n';a_5="WELCOME TO PYTHON";a_6='''WELCOME TO PYTHON''';
a_7=r'this is python';a_8='\newline';a_9=R'literals'
#above are string objects

print(a,a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9)#printind string objects


#NOTE: A white space is also a character is converted into string in python

print("hello" "world")#it is exactly equal to hello world

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



#Note: String supports Unicode standard,Python does not supports Char unlike C++ etc

str_2='a'#this is a string not char
s_1='hello world'#short string
str_3="Strings are Immutable Sequece objects in Python means that their Object value can not change once it has been created."#Long string
print(s_1,str_2,str_3)#prints strings
print(type(s_1));print(type(str_2));print(type(str_3))#String Class
print('hello Python')#directly printing string

#NOTE:Each character or values  is called sub-string of a string. it can be selected by Index value in Python

#NOTE:Index value starts from 0 to n-1(n=number of values in string)from left to right and -1 to -n from right to left

print(s_1[3])#it returns value of substring
print(s_1[1:5])
print(s_1[0:])#it returns from 0 to entire string
print(s_1[-3:-1])
print(s_1[2:-4])
#Methods and Attibutes:

#String Methods:

s_1='Anjan Kumar'#creating an object of a string

print(s_1.capitalize())#Return a copy of the string with its first character capitalized and the rest lowercased.

print(s_1.casefold())#Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.

print(s_1.center(25,'*'))#Return centered in a String of length width along with padding is done using specified character if not given default SPACE

#NOTE: The original string is returned if width is less than or equal to len(s).

print(s_1.count('n'))#Return number of non-overlapping occurrences of substring in range from start to end but these are optional

print(s_1.count('n',0,7))#number of occurances of sub-string in range from start 0 to start 7

print(b'Hello Python'.decode())#returns string from bytes 

print(s_1.encode())#Returns encoded version of string as a bytes object

print(s_1.endswith('r'))#Returns Boolean value True, if string ends with specified suffix else False

print(s_1.endswith('K',4,11))#Suffix in range from 4 to 11

print('hello\tworld\thow\tare\tyou\t'.expandtabs(16))#Return a copy of string where all tab characters replaced by one or more spaces depending on given current column and tabsize

print(s_1.find('a'))#Returns lowest index where sub-string is found within the range from start to stop

#Note: Returns -1 if given sub-string not found in the string

print(s_1.find('a',0,5))#Range over

print(s_1.find('q'))#Returns -1

print(s_1.index('j'))#Returns Integer value as Index of sub-string

print(s_1.index('j',1,6))#From start to stop arguments

#Note: Like find(), index() returns integer where substring found

print(s_1.isalnum())#Returns Boolean value True if all characters are alphanumeric and there is at least one character in a string, False otherwise

#Note: Alphanumeric means alphabetical characters and numrical characters like vehicle numbers

print(s_1.isalpha())##Returns Boolean value True if all characters are alphabetic and there is at least one character in a string, False otherwise

#Note: Alphabetic are those characters defined in the Unicode character database as Letter

print(s_1.isascii())#Returns Boolean value True if all characters in the string are ASCII, False otherwise

#Note: it returns True when string is empty

print(' '.isascii())#Empty string

print(s_1.isdecimal())#Returns True if all characters are decimal characters and there is atleast one character in string, False otherwise

print(s_1.isdigit())#Returns True if all characters are digits and there is atleast one character, False otherwise

print(s_1.isidentifier())#Returns True if string is a valid identifier according to the language definition

a='hello'
print(a.isidentifier())#here 'a' is an string object as an identifier

print(s_1.islower())#Returns True if all cased characters in the string are lowercase and there is atleast one cased character, False otherwise

print(s_1.isnumeric())#Return True if all characters are numeric characters and there is at least one character, False otherwise

print(s_1.isprintable())#Return True if all characters are printable in a string or empty string, False otherwise

print(' '.isprintable())#Returns True because empty string

#Note: A white space is a printable character in the string of python

print(s_1.isspace())#Returns True if there are only white space characters and there is atleast one character in a string, False otherwise

print(s_1.istitle())#Returns True if string is titlecased and there is atleast one character, False otherwise

print(s_1.isupper())#Returns True if all cased characters are uppercase in string and there is atleast one character, False otherwise

print(s_1.join('hello world'))#Return String which concatenation of strings in iterable

#Note: Non-string values not allowed like bytes objects

print(s_1.join('0/,1,/2,/3,/4'))

print(s_1.ljust(15,'#'))#Return string left justified in a string of length width. padding is done by specified fillcharacter but default is space if not given

#Note: if width is less than or equal to length of string, then original string is returned

print(s_1.lower())#Return a copy of string with all cased characters converted to lowercase

print(s_1.lstrip('A'))#Return a copy of string with leading specified characters removed, If not specified character arguments defaults to removing whitespace

print('hello world'.lstrip('eo'))

#Note: character argument is not a prefix; rather all combinations of its values are stripped

print(s_1.rstrip('ra'))#Return a copy of string with trailing characters removed with specified characters, If not specified  arguments, defaults to remove whitespace

#Note: it is stripped from right side or removing from right

print('hello world'.rstrip('deh'))#only d is stripped from the right side

print('hello world'.split())#return a list of words in list format and if any space between words, they seperated pr splitted by comma operator

#Note:Whitespace are regarded as a single seperator default in any word

#Note:If seperation argument is given, consecutive delimeters not grouped together and are deemed to delimit empty strings

print(''.split())#splitting an empty string, returns empty list

print(','.split())#splitting an empty string with a specified seperator returns empty string with siglequote

print('hello welcome to python'.split())#here 3 spaces between the words they are splited by comma operator

#basically spliting can be done by seperation of arguments in split method as mentioned below

print('hello world'.split('e'))#character 'e' is spited in 'hello' and return in the list format

print('hello world'.split('w',))

print('hello world'.split('w',1))#same output as previous

print('hello world'.split('l'))#every 'l' spitted by comma  in each word if present

print('hello world'.split(maxsplit=1))#same as normal split

print('hello<>python<>world<>'.split('<>'))#seperation may consists of multiple characters



#Buit-in Functions for Strings:Conversion

#str():it returns String version of an object. if object not provided, returns empty string

print(str())#Nothing to print(empty string)
print(str(b'hello'))

#ord(): Given a string representing one unicode character that return corresponding an integer

print(ord('@'))#it returns integer representing the Unicode code point of that character

#NOTE: chr() is an inverse ord() and vice versa

#chr(): Given a Integer representing Unicode code point that returns corresponding a character

print(chr(64))#it returns a string
a='hello'
print(a.encode())
print(chr(256))




