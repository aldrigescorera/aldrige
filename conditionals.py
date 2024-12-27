'''age = int(input("Enter your age: "))

# Check if the user is 18 or older
if age >= 18:
    print("You are old enough to drive.")
else:
    years_left = 18 - age
    print(f"You need to wait {years_left} more year(s) to be old enough to drive.")'''


# Exercise 2

'''my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))


if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")
elif my_age < your_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
else:
    print("We are the same age!")'''

#Exercise 3

'''a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is smaller than {b}.")
else:
    print(f"{a} is equal to {b}.")'''


#Exercise 4

'''month = input("Enter the month: ").capitalize()

if month in ["September", "October", "November"]:
    print("Autumn")
elif month in ["December", "January", "February"]:
    print("Winter")
elif month in ["March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month entered. Please enter a valid month name.")'''

#Exercise 5

fruits = ['banana', 'orange', 'mango', 'lemon']

# Get fruit input from the user
fruit = input("Enter a fruit: ").capitalize()

# Check if the fruit exists in the list
if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print(f"The fruit has been added. Updated list: {fruits}")