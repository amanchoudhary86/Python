'''Operators:-

operators are special symbols used to perform operations on variables and values. They can be used to perform arithmetic, comparison, logical, assignment, and other operations.

Types of operators:-
Arithmetic operators-->  +, -, *, /, %, **
Assignment operators-->  =, +=, -=, *=, /=, //=, %=, **=
Comparison operators-->  ==, !=, >, <, >=, <=
Logical operators-->  and, or, not
Identity operators-->  is, is not
Membership operators-->  in, not in
Bitwise operators-->  &, |, ^, ~, <<, >>
Unary operators-->  +(Unary Plus), -(Unary Minus), ~(Unary Bitwise NOT), not(Unary Logical NOT)
Ternary operators-->  value_if_true if condition1 else condition2
Special operators-->  lambda, @, :=, **=, //=

Python operators precedence(The order in which we give them priority order):-

Priority Order(meaning which are executed first in a single line of code), here is that the priority decreases from top to bottom:-

1. Parentheses: `()`
2. Exponentiation: `**`
3. Unary Plus, Unary Minus, Unary Bitwise NOT: `+x`, `-x`, `~x`
4. Multiplication, Division, Floor Division, Modulus: `*`, `/`, `//`, `%`
5. Addition, Subtraction: `+`, `-`
6. Bitwise Shift: `<<`, `>>`
7. Bitwise AND: `&`
8. Bitwise XOR: `^`
9. Bitwise OR: `|`
10. Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
11. Identity: `is`, `is not`
12. Membership: `in`, `not in`
13. Logical NOT: `not`
14. Logical AND: `and`
15. Logical OR: `or`
16. Conditional Expressions: `x if condition else y`
17. Assignment: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `>>=`, `<<=`
18. Assignment Expression: `:=` (also known as Walrus Operator)

Note : Some of the operators which are on the same priority and in that case the left-most one will be executed first and so on from left to right.

Note = Priority order can be changed with the help of paranthesis. 
Example : 2 * 2 + ( 2 + 2 ) --> Here ( 2 + 2 ) will be calculated first because of paranthesis

Need not mug up all of this, we will learn each of these thoroughly and in the most lame and lamen language, for now we will be learning the most basic of these operators
'''

# Arithmetic operators:-
a = 11
b = 5
c = 11
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
'''
Note: The result of floor division is always an integer value(In whole number)
Simply put it is just the simple division as above but it only removes the decimal and the values after that
'''

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

# 3. NOT (not) :-
# It returns True if the condition is False and vice versa
print("not a > b", not a > b)

# Note: It will return False because a > b is True

# Identity Comparison Operators:
# 1. is :-
# It checks if both the variables are the same object in memory
print("a is b", a is c)
# Note: It will return True because a and b are refering to the same memory location. 

# 2. is not :-
# It checks if both the variables are not the same object in memory
print("a is not b", a is not c)
# Note: It will return False because a and b are refering to the same memory location

# Important: Note that if there are two lists which have same content are stored in different memory location.
# Example:
x = [1, 2, 3]
y = [1, 2, 3]
print(a is b) # False

# Membership Test Operators:-
# 1. in :-
# It checks if a value is present in a sequence (like list, tuple, string etc)
print("1 in x", 1 in x)
# Note: It will return True because 1 is present in the list a

# 2. not in :-
# It checks if a value is not present in a sequence (like list, tuple, string etc
print("2 not in y", 2 not in y)
# Note: It will return True because 2 is not present in the list a

'''String: Checks for substring in a String
Dictionary: Checks for the Key in a Dictionary


Bitwise operators:
These operators are used to perform operations on the binary digits of the numbers.

Decimal to binary conversion:

Example:
Let us say that we wish to convert 18 to binary:-
18 / 2 = 9 remainder 0
9 / 2 = 4 remainder 1
4 / 2 = 2 remainder 0
2 / 2 = 1 remainder 0
1 / 2 = 0 remainder 1
So the binary representation of 18 is 10010.

Binary to decimal conversion:
Example:
Let us say that we wish to convert 10010 to decimal:-
we start from the last bit and to the front--> 
(0 * 2⁰) + (1 * 2¹) + (0 * 2²) + (0 * 2³) + (1 * 2⁴) = 18

We can use these conversions with the help of Python itself:
Example:
'''
print(bin(18))
# Output: 0b10010

print(int("0b10010",2))
# Output: 18

'''
1. Bitwise AND (&):
It performs a binary AND operation on each bit of the two operands.

Example:
Let us say that we wish to perform a bitwise AND operation on 18 and 21:-
18 = 10010
21 = 10101
     _____
     10000 = 16

0 and 0 --> 0
0 and 1 --> 0
1 and 0 --> 0
1 and 1 --> 1

2. Bitwise OR (|):
It performs a binary OR operation on each bit of the two operands.

Example:
Let us say that we wish to perform a bitwise OR operation on 18 and 21:-
18 = 10010
21 = 10101
     _____
     10111 = 16

0 or 0 --> 0
0 or 1 --> 1
1 or 0 --> 1
1 or 1 --> 1

3. Bitwise Left Shift (<<):
This operator shifts the binary value of a number to left as per the specified Value
Example:
5 in binary is 101
'''

p = 5
print(p << 1) # Output: 10

'''
Explaination:
101 << 1 = 1010

here the bit row 101 is shifted to the left by one digit and an 0 is added at the end. just like this --> 101 --> 1010 which in decimal is equal to 10

Similarily,
101 << 2 = 10100
101 << 3 = 101000 and so on

4. Bitwise Right Shift (>>):
This operator shifts the binary value of a number to right as per the specified Value
Example:
18 in binary is 10010
'''

p = 18
print(p >> 1) # Output: 9

'''
Explaination:
10010 >> 1 = 1010

Similarily,
10010 >> 2 = 101
10010 >> 3 = 10 and so on

5. Bitwise XOR (^):
It performs a binary XOR operation on each bit of the two operands.

Example:
Let us say that we wish to perform a bitwise XOR operation on 18 and 21:-
18 = 10010
21 = 10101
     _____
     00111 = 7

0 XOR 0 --> 0
0 XOR 1 --> 1
1 XOR 0 --> 1
1 XOR 1 --> 0

Easy way to learn: Same bit--> 0 and different bit--> 1

6. Bitwise NOT (~) :
This operator is used to flip the bits of a number.
Example:
Let us say that we wish to perform a bitwise NOT operation on 18:-
18 = 10010
~18 = -19 
Note: In order to understend this operator, please refer to an external source.

Note: For now just understand that it inverts the bits, meaning it converts all the 0s to 1s and vice versa.
'''