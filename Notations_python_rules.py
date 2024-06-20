#NOTATIONS FOR DOCUMENTATION OF PYTHON:

#::=
#Each rule begins with a name (which is the name defined by the rule).

#name::= it is a sequence of zero or more letters from 'a' through 'z' and underscores.

#A Rule is defined by the name

#VERTICAL BAR|:

#A vertical bar (|) is used to separate alternatives; it is the least binding operator in this notation.

#A vertical bar | is symbol of usage alternatives, either this or that

#SYMBOL*:

#A star (*) means zero or more repetitions of the preceding item

#SYMBOL+:

#likewise, a plus (+) means one or more repetitions.

#SQUARE BRACKETS:

#a phrase enclosed in square brackets ([ ]) means  the enclosed phrase is optional)

#The * and + operators bind as tightly as possible.

#PARENTHESIS():

# parentheses () are used for grouping.

#QUOTES:' "

#Literal strings are enclosed in quotes.

#SPACE:

# White space is only meaningful to separate tokens.

#Rules are normally contained on a single line; rules with many alternatives may be formatted alternatively with each line after the first beginning with a vertical bar.

#In lexical definitions (as the example above), two more conventions are used:

#THREE DOTS:...

#Two literal characters separated by three dots mean a choice of any single character in the given (inclusive) range of ASCII characters.

#Like 'a'...'z'. this means any single character from a to z.

#ANGULAR BRACKETS:

#A phrase between angular brackets (<...>) gives a informal description of the symbol defined;

#e.g., this could be used to describe the notion of ‘control character’ if needed.




