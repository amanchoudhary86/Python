'''A program to return the number of digits.'''

n = int(input("Enter a number"))
counter = 0
while True:
    if n//10>0:
        counter+=1
        n = n//10
    else :
        counter+=1
        break
print (counter)