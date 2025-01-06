import math

#Exercise 1

'''def add_two_numbers(a, b):
    c= a+ b
    return c
result = add_two_numbers(5, 7)
print(result)  # Output: 12'''

#Exercise 2

'''def area_of_circle(radius):
    if radius < 0:
        return "radius cannot be negative"
    return math. pi * radius * radius
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {area}")
'''
#Exercise 3  Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
'''def print_list(items):
    
    for item in items:
        print(item)

example_list = [1, 2, 3, 4, 5]
print_list(example_list)'''

#Exercise 4  Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def evens_and_odds(n):
    
    if n < 0:
        return "The number must be a positive integer."
    
    evens = len([i for i in range(n + 1) if i % 2 == 0])
    odds = n + 1 - evens  
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")


evens_and_odds(100)


