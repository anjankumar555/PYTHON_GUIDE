#Literal Concatenation:
#bytes and string literal concatenation:
#string literal concatenation:
a_1='hello';a_2='world'
print(a_1+a_2)
#string literal concatenation with single or double or triple quotes remains same.
a_3="hello";a_4="world";a_5='hello';a_6='''world'''
print(a_3+a_4+a_5+a_6)
#as well with digits:
print('hello123'+'''world123''')
#To concatenate string literal '+' operator must be used in between literals.
#we can concatenate short strings with long strings as well.
print('Expressions in formatted string literals are treated like regular Python expressions surrounded by parentheses, with a few exceptions.'+"An empty expression is not allowed"
      '''and both lambda and assignment expressions  must be surrounded by explicit parenthesesReplacement expressions can contain line breaks (e.g. in triple-quoted strings), but they cannot contain comments.
        Each expression is evaluated in the context where the formatted string literal appears, in order from left to right.''')
#NOTE1:concatenate is allowed only with strings but not with numeric and Bytes literals.
#NOTE2:we concatenate one literal with corresponding literal is only possible
#concatenate Bytes literals:
print(b'hello'+b'world'+b"hello python"+b'''hello python world''')
#cancatenate Unicode Literals:
print(u'ఎక్కడ'+u'ఎవరు')
#concatenate strings instead numbers:
print('1'+'4'+'3')#these are numbers enclosed in quotes treated as strings in PYTHON.
