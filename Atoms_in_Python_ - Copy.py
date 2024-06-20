#GENERATOR EXPRESSIONS:it is a compact generator notation in parentheses. it is an expression that returns iterator.
#it is normal expression followed by a FOR clause loop variable, range  and IF clause (optional always)
#Generator Expressions syntax is same as comprehensions except enclosed in curly brackets.
#SYNTAX:(Expression Comprehension for)
#it returns a new generator object
print((x**2 for x in [1,2,3,4,5]))#first expression and then for clauses in iterable.
print((y+2 for y in {1,2,3,4,5}))#first expression and then for clauses in iterable.
print(a*b for a in [1,2,3] for b in [4,5,6])
print(c*d for c in range(4) for d in range(6))
print(c*d for c in range(2) for d in range(c,c+4))
print((x**2 for x in [1,2,3,4,5] if x>5))
print(sum(i*i for i in range(10)))#it is GENERATOR EXPRESSION.
def gen(a):
    yield from 3*5
    return
gen(6)
