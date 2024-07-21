# Loops :-

# Loops are a fundamental programming construct that allows you to execute a block of code repeatedly based on certain conditions. In short loops allow the programmer to execute a particular block of code multiple times.

# In Python, there are several types of loops, including for loops, while loops, and nested loops (loops inside loops).

# for loop:-
# A type of loop that iterates(goes through) over a sequence (such as a list, tuple, or string) and executes a block of code for each item in the sequence.

# Example:
for i in range(5):
    print(i)

# Output:-
# 0
# 1
# 2
# 3
# 4

#for i in range(5): This is the loop header, which consists of the for keyword, a variable i, and an iterable range(5).
# range(5) generates a sequence of numbers from 0 to 4.
# The loop will iterate over this sequence, assigning each value to the variable i in turn.
# The code indented under the loop header (print(i)) will be executed for each iteration.

# while loop:-
# A type of loop that executes a block of code repeatedly while a certain condition is true.
# Example:
i = 0
while i < 5:
    print(i)
    i += 1

# Output:-
# 0
# 1
# 2
# 3
# 4

# i+=1 is the same as i = i + 1 and, it can also be simply written as i--
# similarily,

# i-=1 is the same as i = i - 1, and it can also be simply written as i--

# i*=2 is the same as i = i * 2
# i/=2 is the same as i = i / 2
# i%=2 is the same as i = i % 2
# i**=2 is the same as i = i ** 2
# i//=2 is the same as i = i // 2