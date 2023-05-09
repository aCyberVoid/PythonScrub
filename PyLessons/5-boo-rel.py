# ╭─── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ───╮
#    BOOLEAN EXPRESSIONS
#             &
#    RELATIONAL OPERATORS
# ╰─── ⋅ ⋅ ─── ✩ ─── ⋅ ⋅ ───╯

# In Python 3, Boolean expressions and relational operators are used to compare values and determine the relationship between them. A Boolean expression is an expression that evaluates to either True or False. Relational operators, such as >, <, ==, and !=, are used to compare two values and determine whether a specific relationship holds between them. For example, the expression 5 > 3 evaluates to True because 5 is greater than 3, while the expression 5 < 3 evaluates to False because 5 is not less than 3.

bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9
print(bool1,bool2,bool3,bool4)
# Type() specifies the type of function
print(type(bool1))

bool5 = "True"
print(type(bool5))

greater_than = 7 > 5
less_than = 5 < 7
greater_than_or_equal_to = 7 >= 7
less_than_or_equal_to = 7 <= 7
# True statement
test_and = (7 > 5) and (5 < 7)
# False Statement
test_and2 = (7 >5) and (5 > 7)
# Both are True
test_or = (7 > 5) or (5 < 7)
# One or the other is True
test_or2 = (7 >5) or (5 > 7)
# Setting a statement to the opposite
test_not = not True
