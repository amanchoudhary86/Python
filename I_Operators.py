# Operators:-

# operators are special symbols used to perform operations on variables and values. They can be used to perform arithmetic, comparison, logical, assignment, and other operations.

# Types of operators:-
# Arithmetic operators-->  +, -, *, /, %, **
# Assignment operators-->  =, +=, -=, *=, /=, //=, %=, **=
# Comparison operators-->  ==, !=, >, <, >=, <=
# Logical operators-->  and, or, not
# Identity operators-->  is, is not
# Membership operators-->  in, not in
# Bitwise operators-->  &, |, ^, ~, <<, >>
# Unary operators-->  +(Unary Plus), -(Unary Minus), ~(Unary Bitwise NOT), not(Unary Logical NOT)
# Ternary operators-->  value_if_true if condition1 else condition2
# Special operators-->  lambda, @, :=, **=, //=

# Python operators precedence(The order in which we give them priority order):-

# Priority Order(meaning which are executed first in a single line of code), here is that the priority decreases from top to bottom:-

# 1. Parentheses: `()`
# 2. Exponentiation: `**`
# 3. Unary Plus, Unary Minus, Unary Bitwise NOT: `+x`, `-x`, `~x`
# 4. Multiplication, Division, Floor Division, Modulus: `*`, `/`, `//`, `%`
# 5. Addition, Subtraction: `+`, `-`
# 6. Bitwise Shift: `<<`, `>>`
# 7. Bitwise AND: `&`
# 8. Bitwise XOR: `^`
# 9. Bitwise OR: `|`
# 10. Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
# 11. Identity: `is`, `is not`
# 12. Membership: `in`, `not in`
# 13. Logical NOT: `not`
# 14. Logical AND: `and`
# 15. Logical OR: `or`
# 16. Conditional Expressions: `x if condition else y`
# 17. Assignment: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `>>=`, `<<=`
# 18. Assignment Expression: `:=` (also known as Walrus Operator)

# Note : Some of the operators which are on the same priority and in that case the left-most one will be executed first and so on from left to right.

# Note = Priority order can be changed with the help of paranthesis. 
# Example : 2 * 2 + ( 2 + 2 ) --> Here ( 2 + 2 ) will be calculated first because of paranthesis

# Need not mug up all of this, we will learn each of these thoroughly and in the most lame and lamen language, for now we will be learning the most basic of these operators

# Arithmetic operators:-
a = 11
b = 5
print("a", a)
print("b", b)

#1. Addition:-
print("a + b = ", a + b )

#2. Subtraction:-
print("a - b = ", a - b )

#3. Multiplication:-
print("a * b = ", a * b )

#4. Division:-
print("a / b = ", a / b )
# Note: The result of division is always a float value(In decimal)

#5. Floor Division:-
print("a // b = ", a // b )
# Note: The result of floor division is always an integer value(In whole number)
# Simply put it is just the simple division as above but it only removes the decimal and the values after that

# Example:-
# 11 / 5 = 2.2
# 11 // 5 = 2

# 6. Modulus:- 
# It simply returns the remainder
print("a % b = ", a % b )
# Example:
# 11 divided by 5 gives the remainder 1, so a % b = 11 % 5 = 1 <-- for reference only

# 7. Exponentiation:-
print("a ** b = ", a ** b )
# a ** b is simply a to power b 

# Logical Operators:
# 1. AND (and) :-
# It returns True if both the conditions are True
print("a > b and a < b", a > b and a < b )
# Note: It will return False because a is not less than b

# Example:-
# a = 11
# b = 5
# a > b and a < b is False because a is not less than b

# 2. OR (or) :-
# It returns True if either of the conditions is True
print("a > b or a < b", a > b or a < b )

# Bitwise operators:
# These operators are used to perform operations on the binary digits of the numbers.

# Decimal to binary conversion:

# Example:
# Let us say that we wish to convert 18 to binary:-
# 18 / 2 = 9 remainder 0
# 9 / 2 = 4 remainder 1
# 4 / 2 = 2 remainder 0
# 2 / 2 = 1 remainder 0
# 1 / 2 = 0 remainder 1
# So the binary representation of 18 is 10010.

# Binary to decimal conversion:
# Example:
# Let us say that we wish to convert 10010 to decimal:-
# we start from the last bit and to the front--> 
# (0 * 2⁰) + (1 * 2¹) + (0 * 2²) + (0 * 2³) + (1 * 2⁴) = 18

# We will be learning other operaators in the further modules as we go, so stay tuned.