# Exercise 1    /  how to iterate from 0 to 10 using both a for loop and a while loop in Python:

'''for i in range(11):  # range(11) generates numbers from 0 to 10
    print(i)'''

'''i=0
while i <= 10:
    print(i)
    i += 1'''

# Exercise 2    /Iterate 10 to 0 using for loop, do the same using while loop.

'''for i in range(10, -1, -1):  # Start at 10, stop at -1 (exclusive), step by -1
    print(i)

i=10
while i >= 10:
    print(i)
    i -= 1'''

# Exercise 3    /Iterate 10 to 0 using for loop, do the same using while loop.

'''for i in range(11):  # Loop from 1 to 7
    print(' # '* i )'''

# Exercise 4
'''for i in range(11):  # Loop from 1 to 7
    print(' # ' * 5 )'''

# Exercise 5 

'''for i in range(11):
    print(f'{i} x {i} = {i * i}')'''

# Exercise 6   / Use for loop to iterate from 0 to 100 and print the sum of all numbers.

'''sum = 0

for i in range(101):
    sum += i

    print(sum)'''

# Exercise 7    / Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.


even = 0
odd = 0

for i in range(101):
    if i % 2 == 0:
        even += i
        print(even)
    else :
        odd += i
        print(odd)   


# Exercise 8  / 